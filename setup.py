import os
from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.realpath(__file__))

VERSION = '2.1.0'
PACKAGE_NAME = 'Simulated-Quantum-Computer'
AUTHOR = 'Cameron Matthew'
AUTHOR_EMAIL = 'cambobmat@icloud.com'
URL = 'https://github.com/Quantum-Computing-GP-3/Simulated-Quantum-Computer'
LICENSE = 'GPL-3.0'

DESCRIPTION = 'A series of quantum computer simulations for Edinburgh University School of Physics and Astronomy "Quantum Computing Project" course'
LONG_DESC_TYPE = "text/markdown"
README_PATH = os.path.join(HERE, "README.md")

if os.path.isfile(README_PATH):
    with open(README_PATH) as f:
        LONG_DESCRIPTION = f.read()

REQUIREMENETS = os.path.join(HERE, "requirements.txt")
INSTALL_REQUIRES = []

DATA_FILES = [('resource', ['resource/mainpage.ui', 'resource/grover.ui'])]

if os.path.isfile(REQUIREMENETS):
    with open(REQUIREMENETS) as f:
        INSTALL_REQUIRES = f.read().splitlines()

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      data_files=DATA_FILES,
      entry_points={
          'console_scripts': [
                "qStart = frontend.gui:main",  # Start the GUI
                "grover = algorithms.grover:main",  # Run grover from command line
                "shor = algorithms.shor:main"  # Run shor from command line
              ]
          }
      )
