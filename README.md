[![Build Status](https://travis-ci.org/FreeJournal/freejournal.svg?branch=develop)](https://travis-ci.org/FreeJournal/freejournal) [![Coverage Status](https://coveralls.io/repos/FreeJournal/freejournal/badge.svg?branch=develop)](https://coveralls.io/r/FreeJournal/freejournal?branch=coveralls)
# Free-Journal
Project Homepage: http://freejournal.org/
Example Node: http://freejournal.io/

## Prerequisites

The first step to installing FreeJournal is to ensure you have:
- A Linux-based operating systems (for security reasons, we do not support Windows)
- Python 2.7.3+
- [PyBitmessage](https://github.com/Bitmessage/PyBitmessage/)
- Python 2.x
- python-pip (the pip command)
- [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)
- [FreeNet](https://freenetproject.org) (install script provided)

If you are on Windows, you can still browse one of many existing FreeJournal nodes.
Consult a list on our website.

To install database, documentation, and other library requirements, run
``sudo pip install -r requirements.txt`` on the root directory.

After this, you should perform the required Freenet and Bitmessage setup using:
``sudo ./freejournal_cli.py install all`` on a Debian-compatible distribution.

## Generating Documentation

To generate API documentation, simply run
``make install`` in the ``docs`` subfolder to install required dependencies, then run
``make html`` to generate documentation in HTML form, output to the build directory.

## Running FreeJournal - Command Line

### Creating and publishing a collection

Modify the following example commands to create and publish a collection:
```
./freejournal_cli.py putcollection whee 1,2,3 "This is a TEST" "nothing to see here" "nothing,to" btc123
Collection inserted with address/ID [BM-2cVBBDezMcgoAHMkNzMswkc3xZRMFFvKeV
./freejournal_cli.py publishcollection whee BM-2cVBBDezMcgoAHMkNzMswkc3xZRMFFvKeV
```

For more command usage instructions, run ``./freejournal_cli.py`` with no arguments.

## Running FreeJournal Unit Tests

Simply ``coverage run --omit=*/python?.?/*,*/site-packages/*,*__init__*,test_*,*Freenet* -m unittest discover unittests`` 
in the root directory after installing the required prerequisites to run all tests with coverage.

## Running FreeJournal - The Network

To start pulling and pushing collections to and from the network, use the following two commands:

``./freejournal_cli.py keepalive`` and ``./freejournal_cli.py listen``


## Running FreeJournal - Web interface

After configuring the web interface in config.py, use `./freejournal_cli.py webapp` to run an insecure
 development server.  Hardened deployments should use the advanced deployment guides on the Flask 
website.
