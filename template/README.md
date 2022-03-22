# Template Python Package
Used to illustrate a minimal package structure and shows how we can manage dependencies and use a command line interface.

# Package Structure
A minimal python package requires this structure:
```
template/
  template_package/
    __init__.py
    console_entry_point.py
  README.md
  requirements.txt
  setup.py
```
- The `template_package` directory contains all the runnable python modules (the meat of the code), as well as a mandatory `__init__.py` file (which can be left empty).
- The `README.md` file contains long-form documentation for the package. See [Make a README](https://www.makeareadme.com/).
- The `requirements.txt` file contains a list of all third party python packages required to run this package. These are automatically installed by pip when this package is installed.
- The `setup.py` file is the file used to install our package. It contains key package information such as version, authors, dependencies, entry points etc...

# Installation
Navigate to tamplate directory and run
```bash
> pip install -e .
```
This will install all the necessary python packages and will expose the console scripts entry point "sample".
This means you can now run the following in the console:
```bash
> sample
This script has been run
```

