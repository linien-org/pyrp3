from distutils.core import Extension, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name="pyrp3",
    version="1.1.0",
    description="Python utilities for redpitaya",
    author="Pierre Cladé",
    author_email="pierre.clade@upmc.fr",
    maintainer="Bastian Leykauf",
    maintainer_email="leykauf@physik.hu-berlin.de",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=["pyrp3", "pyrp3.enum"],
    install_requires=["myhdl", "rpyc", "cached_property", "numpy"],
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
