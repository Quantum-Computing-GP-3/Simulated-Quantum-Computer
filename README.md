# Simulated Quantum Computer
A series of quantum computer algorithm simulations for Edinburgh University School of Physics and Astronomy "Quantum Computing Project" course.

## Contents
- [Package Structure](#package-structure)
- [Usage](#usage)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Entry Points](#entry-points)

## Package Structure
This repository has the following structure:
```
Simulated-Quantum-Computer/
  algorithms/
    ...
  frontend/
    ...
  gates/
    ...
  groverTensorRepresentation/
    ...
  helpers/
    ...
  resource/
    ...
  LICENSE
  README.md
  requirements.txt
  setup.py
```
- `algorithms` is a python package containing main functions for the algorithms which we want to simulate.
- `frontend` contains the PyQt5 GUI application used to launch and configure the simulator.
- `gates` contain definitions of a series of useful quantum gates- which are used in combination to form an algorithm.
- `groverTensorRepresentation` is our original attempt at a Grover's algorithm simulator using a generalised quantum gate object. It works if you know the matrix representation of all the gates you wish to use, but it is much slower than the gates defined in the `gates` package.
- `helpers` is a library containing useful helper functions which we repeatedly use throughout our code.
- `resource` is a folder storing the PyQt '.ui' files which are used to render the GUI.
- The `README.md` file contains long-form documentation for the package. See [Make a README](https://www.makeareadme.com/).
- The `requirements.txt` file contains a list of all third party python packages required to run this package. These are automatically installed by pip when this package is installed.
- The `setup.py` file is the file used to install our package. It contains key package information such as version, authors, dependencies, entry points etc...

## Usage

### Requirements
- [Python 3.8-3.10](https://www.python.org/downloads/)
- [pip 22.0.4](https://pip.pypa.io/en/stable/installation/)

### Installation
Once the Simulated-Quantum-Computer source code is stored locally on your system, you can install the package using pip. This automatically manages all of the external python packages that Simulated-Quantum-Computer relies on.

To install package dependencies and console entry points, navigate to the `Simulated-Quantum-Computer` directory in your terminal/console and run:

```bash
$ pip install -e .
```
We add the `-e` flag so that the python modules can be edited without having to reinstall.

To verify that the package has been installed, run:
```bash
$ pip show Simulated-Quantum-Computer
```

This should output something like this:
```
Name: Simulated-Quantum-Computer
Version: 3.0.0
Summary: A series of quantum computer simulations for Edinburgh University School of Physics and Astronomy "Quantum Computing Project" course
Home-page: https://github.com/Quantum-Computing-GP-3/Simulated-Quantum-Computer
Author: Cameron Matthew
Author-email: cambobmat@icloud.com
License: GPL-3.0
Location: c:\users\cambo\cameron matthew projects\simulated-quantum-computer
Requires: colour, matplotlib, numpy, pathlib, PyQt5
Required-by:
```

You may need to uninstall then reinstall this package if you edit `setup.py`. To uninstall run:
```bash
$ pip uninstall Simulated-Quantum-Computer
```
### Entry Points
This package is configured such that the simulation can run from the command line using custom commands. To launch the GUI simply run:
```bash
$ qStart
```

If you wish to run individual python modules independently, you must modify the usual python cli syntax as our package uses the pip package import style. To run a module called `example.py`, run the following command in your terminal/powershell:
```bash
$ python -m relative.path.to.module
```

