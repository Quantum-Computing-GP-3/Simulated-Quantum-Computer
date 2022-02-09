import os
from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.realpath(__file__))

VERSION = '0.0.0'
PACKAGE_NAME = 'template_package'
AUTHOR = 'Cameron Matthew'
AUTHOR_EMAIL = 'cambobmat@icloud.com'
URL = 'https://github.com/Quantum-Computing-GP-3/Simulated-Quantum-Computer'
LICENSE = 'GPL-3.0'

DESCRIPTION = 'Short package description'
LONG_DESC_TYPE = "text/markdown"
README_PATH = os.path.join(HERE, "README.md")

if os.path.isfile(README_PATH):
    with open(README_PATH) as f:
        LONG_DESCRIPTION = f.read()

REQUIREMENETS = os.path.join(HERE, "requirements.txt")
INSTALL_REQUIRES = []

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
      entry_points={
          'console_scripts': [
              'sample = template_package.console_entry_point:main'
              ]
          }
      )
