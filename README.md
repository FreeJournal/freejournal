# Free-Journal
https://travis-ci.org/FreeJournal/freejournal.svg?branch=fixTravisAndUnittests
Project Homepage: http://freejournal.org/
Example Node: http://freejournal.io/

## Prerequisites

The first step to installing FreeJournal is to ensure you have:
- A Linux-based operating systems (for security reasons, we do not support Windows)
- Python 2.x
- [PyBitmessage](https://github.com/Bitmessage/PyBitmessage/)
- [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)
- [FreeNet](https://freenetproject.org)

If you are on Windows, you can still browse one of many existing FreeJournal nodes.
Consult a list on our website.

Run sh install.sh to install the required Python-based prerequisites, then modify
config.py to change your local node settings.

## Generating Documentation

To generate API documentation, simply `sh generate_docs.sh` and check the `docs` folder
for output.

## Running FreeJournal

Coming soon

## Running FreeJournal Unit Tests

Simply `python run_tests.py` in the root directory after installing the required
prerequisites.
