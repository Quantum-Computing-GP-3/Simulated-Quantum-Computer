# Simulated Quantum Computer
A series of quantum computer simulations for Edinburgh University School of Physics and Astronomy "Quantum Computing Project" course.

## Contents
- [Package Structure]()
- [Usage]()
  - [Requirements]()
  - [Installation]()
  - [Entry Points]()

## Package Structure
A minimal python package requires this structure:
```
Simulated-Quantum-Computer/
  pabloSim/
    __init__.py
    ...
  stewartSim/
    __init__.py
    ...
  README.md
  requirements.txt
  setup.py
```
- `stewartSim` Is a python package containing version 2.0 of the simulated quantum computer, in this version each operator has a bespoke `acts_on` method allowing for decreased computation time.
- `pabloSim` Is a python package containing version 1.0 of the simulated quantum computer, implementing our first attempy at grover's algorithm
- The `README.md` file contains long-form documentation for the package. See [Make a README](https://www.makeareadme.com/).
- The `requirements.txt` file contains a list of all third party python packages required to run this package. These are automatically installed by pip when this package is installed.
- The `setup.py` file is the file used to install our package. It contains key package information such as version, authors, dependencies, entry points etc...

## Usage

### Requirements
- [Python 3.8](https://www.python.org/downloads/) or greater
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation
To install package dependencies and console entry points, navigate to the `Simulated-Quantum-Computer` directory in your terminal/console and run:

```bash
$ pip install -e .
```
We add the `-e` flag so that the python modules can be edited without having to reinstall.

You may need to uninstall then reinstall this package if you edit `setup.py`. To uninstall run:
```bash
$ pip uninstall Simulated-Quantum-Computer
```
### Entry Points
This package is configured such that the simulation can run from the command line using custom commands. To run Grover's algorithm as written in pabloSim, then run:
```bash
$ pabloSim
```
To run Grover's algorithm as written in stewartSim, run:
```bash
$ stewartSim
```

