import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='shadowtrackr',
    version='1.1.1',
    packages=setuptools.find_packages(),
    url='https://github.com/shadowtrackr/python_API',
    license='MIT',
    author=' Bas van Schaik',
    author_email='bas@shadowtrackr.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='A python API for ShadowTrackr',
    install_requires=[
         'requests'
      ]
)