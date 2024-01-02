# pyrp3

Python 3 port (using [`2to3`](https://docs.python.org/3/library/2to3.html)) of
[PyRedPitaya](https://github.com/clade/PyRedPitaya>) library in the `pyrp3` namespace.

Note: The following is a copy of the Readme from the original repo and might not work 
with this version of the library.

## Overview

This package provides a library to access the [Red Pitaya](http://redpitaya.com/) registers.
This library consist of a C library (`libmonitor.c`) and a `ctypes` interface on the Python side. 

An object-oriented interface to the different application (scope, generator, PID, AMS, ...) is 
provided. This interface is implemented using Python properties (see usage below) and can quickly be
extended to your own application. 

A `rpyc` server is used in order to communicate with your computer. The interface is the same on the
computer as the one on the board.

## Installation

To install `pyrp3`` on any machine, run the command:

```bash
  pip3 install pyrp3
```

## Usage

You need to have Python installed on you Red Pitaya. 

### Interactive Python

Logging onto the redpitaya using ssh, one can start the ipython shell and run :

```python

    from pyrp3.board import RedPitaya

    redpitaya = RedPitaya()

    print(redpitaya.ams.temp) # Read property
    redpitaya.hk.led = 0b10101010 # Write property
```

### Remote access

You need to install the `pyrp3` package on your PC as well as `rpyc`: 

```bash
    rpyc_server
```

On the computer (replace `REDPITAYA_IP` by the string containing the IP address) : 

```python
    from rpyc import connect
    from pyrp3.pc import RedPitaya

    conn = connect(REDPITAYA_IP, port=18861)
    redpitaya = RedPitaya(conn)

    print(redpitaya.read(0x40000000)) # Direct access

    print(redpitaya.ams.temp) # Read property
    redpitaya.hk.led = 0b10101010 # Write property

    from time import sleep
    from pylab import *

    redpitaya.scope.setup(frequency = 100, trigger_source=1)
    sleep(100E-3)
    plot(redpitaya.scope.times, redpitaya.scope.data_ch1)
    show()
```