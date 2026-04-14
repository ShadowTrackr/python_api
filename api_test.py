"""
shadowtrackr_test.py
--------------------
On every run this script:
  1. Pulls the latest shadowtrackr release from PyPI  (pip install --upgrade).
  2. Reports the installed version.
  3. Runs a structured test suite against every public API function.

Requirements
------------
  Python 3.8+  (no extra deps needed beyond what shadowtrackr pulls in)

Usage
-----
  python shadowtrackr_test.py --api-key YOUR_KEY [--proxy HOST:PORT]
"""

import argparse
import importlib
import json
import subprocess
import sys
import textwrap
import traceback
import urllib.request
from dataclasses import dataclass, field
from typing import Callable, List, Optional

# ── colours (graceful fallback) ──────────────────────────────────────────────
try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
    GREEN  = Fore.GREEN
    RED    = Fore.RED
    YELLOW = Fore.YELLOW
    CYAN   = Fore.CYAN
    RESET  = Style.RESET_ALL
except ImportError:
    GREEN = RED = YELLOW = CYAN = RESET = ""

PYPI_PACKAGE = "shadowtrackr"
PYPI_JSON    = f"https://pypi.org/pypi/{PYPI_PACKAGE}/json"


# ═══════════════════════════════════════════════════════════════════════════
# Step 1 – upgrade from PyPI and report the version
# ═══════════════════════════════════════════════════════════════════════════

def upgrade_from_pypi() -> str:
    """
    Run  pip install --upgrade shadowtrackr  then return the version that
    ended up installed.  Falls back to importlib.metadata if the PyPI API
    is unreachable.
    """
    print(f"{CYAN}── Upgrading package from PyPI ─────────────────────{RESET}")

    # -- check latest version available on PyPI --------------------------------
    latest = _pypi_latest_version()
    if latest:
        print(f"  Latest on PyPI : {YELLOW}{latest}{RESET}")

    # -- pip install -----------------------------------------------------------
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "--upgrade", "--quiet", PYPI_PACKAGE],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result.returncode != 0:
        print(f"{RED}pip install failed:{RESET}\n{result.stderr}", file=sys.stderr)
        sys.exit(1)

    # -- report installed version ---------------------------------------------
    installed = _installed_version()
    status = f"{GREEN}already up-to-date{RESET}" if installed == latest else f"{GREEN}installed{RESET}"
    print(f"  Installed      : {GREEN}{installed}{RESET}  ({status})")
    return installed


def _pypi_latest_version() -> Optional[str]:
    try:
        with urllib.request.urlopen(PYPI_JSON, timeout=10) as resp:
            data = json.loads(resp.read())
            return data["info"]["version"]
    except Exception:
        return None


def _installed_version() -> str:
    try:
        import importlib.metadata as meta
        return meta.version(PYPI_PACKAGE)
    except Exception:
        return "unknown"


# ═══════════════════════════════════════════════════════════════════════════
# Step 2 – tiny test framework (no pytest dependency)
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class TestResult:
    name: str
    passed: bool
    message: str = ""
    exception: Optional[Exception] = None


@dataclass
class TestSuite:
    results: List[TestResult] = field(default_factory=list)

    def add(self, name: str, fn: Callable) -> None:
        print(f"  {YELLOW}> {name}{RESET} ... ", end="", flush=True)
        try:
            fn()
            self.results.append(TestResult(name=name, passed=True))
            print(f"{GREEN}PASS{RESET}")
        except AssertionError as exc:
            self.results.append(TestResult(name=name, passed=False,
                                           message=str(exc), exception=exc))
            print(f"{RED}FAIL{RESET}  {exc}")
        except Exception as exc:
            self.results.append(TestResult(name=name, passed=False,
                                           message=str(exc), exception=exc))
            print(f"{RED}ERROR{RESET}")
            traceback.print_exc()

    def summary(self) -> None:
        total  = len(self.results)
        passed = sum(r.passed for r in self.results)
        failed = total - passed
        print(f"\n{CYAN}── Summary ─────────────────────────────────────────{RESET}")
        print(f"  Total : {total}  |  {GREEN}Passed : {passed}{RESET}  |  "
              f"{(RED if failed else '')}Failed : {failed}{RESET}")
        if failed:
            print(f"\n{RED}Failed tests:{RESET}")
            for r in self.results:
                if not r.passed:
                    print(f"  x {r.name}: {r.message}")
        sys.exit(0 if failed == 0 else 1)


# ═══════════════════════════════════════════════════════════════════════════
# Step 3 – the actual tests
# ═══════════════════════════════════════════════════════════════════════════

def run_tests(api_key: str, proxy: Optional[str]) -> None:
    # Re-import after the upgrade so we always exercise the freshly installed code
    for mod in list(sys.modules.keys()):
        if mod == "shadowtrackr" or mod.startswith("shadowtrackr."):
            del sys.modules[mod]
    importlib.invalidate_caches()

    from shadowtrackr import ShadowTrackr  # noqa: PLC0415

    suite = TestSuite()
    print(f"\n{CYAN}── Running tests ───────────────────────────────────{RESET}")

    st: Optional[ShadowTrackr] = None

    # ── construction ────────────────────────────────────────────────────────
    def test_instantiation():
        nonlocal st
        st = ShadowTrackr(api_key=api_key)
        assert st is not None, "Constructor returned None"

    suite.add("Instantiation – ShadowTrackr(api_key=...)", test_instantiation)

    # ── proxy helper ────────────────────────────────────────────────────────
    def test_set_proxy_noop():
        assert hasattr(st, "set_proxy"), "set_proxy method missing"
        st.set_proxy("127.0.0.1:8080")   # validates the call; no real traffic

    suite.add("set_proxy() – accepts host:port without raising", test_set_proxy_noop)

    if proxy:
        def test_set_custom_proxy():
            st.set_proxy(proxy)
        suite.add(f"set_proxy() – user-supplied proxy ({proxy})", test_set_custom_proxy)

    # ── query method shape ───────────────────────────────────────────────────
    def test_query_callable():
        assert callable(getattr(st, "query", None)), \
            "query() method missing or not callable"

    suite.add("query() – method exists and is callable", test_query_callable)

    # ── live query tests ─────────────────────────────────────────────────────
    LIVE_QUERIES = [
        ("query – certificates by issuer (last 10d)",
         "index=certificates by issuer earliest=-10d"),
        ("query – problem hosts (last month)",
         "index=hosts problem=yes earliest=-1m"),
        ("query – hosts with RDP open (port 3389)",
         "index=hosts ports=3389"),
        ("query – DNS SPF TXT records",
         'index=dns rrtype=txt rrdata="*spf*"'),
        ("query – websites running nginx",
         "index=websites https_server=*nginx*"),
        ("query – certificates with grade A (last month)",
         "index=certificates grade=A earliest=-1m"),
        ("query – all WHOIS records",
         "index=whois"),
    ]

    for label, q in LIVE_QUERIES:
        def make_test(query=q):
            def _test():
                result = st.query(query)
                assert result is not None, "query() returned None"
                assert isinstance(result, (list, dict)), (
                    f"Expected list or dict, got {type(result).__name__}"
                )
            return _test
        suite.add(label, make_test())

    # ── edge-case: empty result is still a valid container ───────────────────
    def test_query_nonexistent_host():
        result = st.query(
            "index=hosts hostname=this.host.definitely.does.not.exist.invalid"
        )
        assert isinstance(result, (list, dict)), (
            f"Expected list or dict for empty result, got {type(result).__name__}"
        )

    suite.add(
        "query – non-existent host returns empty list/dict (not an error)",
        test_query_nonexistent_host,
    )

    # ── public API surface ───────────────────────────────────────────────────
    def test_public_api_surface():
        required = ["query", "set_proxy"]
        missing  = [m for m in required if not hasattr(st, m)]
        assert not missing, f"Missing public methods: {missing}"

    suite.add("Public API surface – all documented methods present",
              test_public_api_surface)

    suite.summary()


# ═══════════════════════════════════════════════════════════════════════════
# Entry point
# ═══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Upgrade shadowtrackr from PyPI, then run its test suite.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python shadowtrackr_test.py --api-key abc123
              python shadowtrackr_test.py --api-key abc123 --proxy 10.0.0.1:8080
        """),
    )
    parser.add_argument(
        "--api-key", required=True,
        help="Your ShadowTrackr API key "
             "(https://shadowtrackr.com/usr/settings?s=api)",
    )
    parser.add_argument(
        "--proxy", default=None,
        help="Optional HTTP proxy, e.g. 10.0.0.1:8080",
    )
    args = parser.parse_args()

    upgrade_from_pypi()
    run_tests(api_key=args.api_key, proxy=args.proxy)


if __name__ == "__main__":
    main()