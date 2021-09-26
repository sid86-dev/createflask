from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.0.1'
DESCRIPTION = 'Python package for creating flaskapp'
LONG_DESCRIPTION = 'Now create your flask development environment with 2 simple commands'

# Setting up
setup(
    name="piencrypt",
    version=VERSION,
    author="Throttlerz (Siddhartha Roy)",
    author_email="<sid86harth@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['tqdm'],
    keywords=['python', 'web development', 'createapp',
              'automation', 'flask', 'python flask'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
