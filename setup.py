import os
from distutils.command.build import build
from distutils.command.install import install
from distutils.core import setup
from pathlib import Path

from PyRedPitaya import __version__

# If we want to overrid the build processe
# For example, to compile de libmonitor and install it
# Install libmonitor only for redpitaya, i.e. when

build_dir = "monitor/"


def compile_libmonitor():
    cwd = os.getcwd()  # get current directory
    try:
        os.chdir(build_dir)
        os.system("make clean")
        os.system("make all")
    finally:
        os.chdir(cwd)


def install_libmonitor(prefix=""):
    cwd = os.getcwd()  # get current directory
    try:
        os.chdir(build_dir)
        os.system("make install INSTALL_DIR={prefix}".format(prefix=prefix))
    finally:
        os.chdir(cwd)


class lib_build(build):
    def run(self):
        compile_libmonitor()
        build.run(self)


class lib_install(install):
    def run(self):
        compile_libmonitor()
        install_libmonitor(self.prefix)


#        install.run(self)


cmdclass = {}
cmdclass["lib_build"] = lib_build
cmdclass["lib_install"] = lib_install

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()


setup(
    name="PyRedPitaya",
    version=__version__,
    description="Python utilities for redpitaya",
    author="Pierre Cladé",
    author_email="pierre.clade@upmc.fr",
    maintainer="Bastian Leykauf",
    maintainer_email="leykauf@physik.hu-berlin,de",
    long_description=long_description,
    long_description_content_type="text/rst",
    packages=["PyRedPitaya", "PyRedPitaya.enum"],
    install_requires=["myhdl", "rpyc", "cached_property", "numpy"],
    cmdclass=cmdclass,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["redpitaya", "FPGA", "zynq"],
)
