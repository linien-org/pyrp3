import re
from distutils.core import Extension, setup
from pathlib import Path

# from https://stackoverflow.com/a/7071358/2750945
VERSIONFILE = "pyrp3/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name="pyrp3",
    version=verstr,
    description="Python utilities for redpitaya",
    author="Pierre Cladé",
    author_email="pierre.clade@upmc.fr",
    maintainer="Bastian Leykauf",
    maintainer_email="leykauf@physik.hu-berlin.de",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=["pyrp3"],
    python_requires=">=3.5",
    install_requires=[
        "myhdl>=0.11",
        "rpyc>=4.0,<5.0",
        "cached_property>=1.5.2",
        "numpy>=1.11.0",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["redpitaya", "FPGA", "zynq"],
    ext_modules=[Extension("monitor", ["monitor/monitor.c"])],
)
