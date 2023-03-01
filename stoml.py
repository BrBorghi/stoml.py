#! /usr/local/bin/python3
"""
to get the value of a key from a file called filename and export it as a Bash environment variable, run
$ export MYVALUE=`stoml filename key`

TOML files can have sections (tables). Keys in sections are referred to with dotted paths. Only one level is permitted.
$ export MYSECTIONVALUE=`stoml filename mysection.key`
"""

import argparse
import tomllib
import logging
import sys

# 0. Setup
## 0.1 Use logging to log errors. Time is logged in ISO 8601 format
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
)

## 0.2 Define command-line arguments
parser = argparse.ArgumentParser(description=__doc__,
                            formatter_class=argparse.RawDescriptionHelpFormatter) # display the script docstring on --help
parser.add_argument("filename", help="TOML file")
parser.add_argument("key", help="get value for key")
parser.add_argument("-V", "--Version", help="show current version", action="store_true")

# 1. Get command line arguments
args = parser.parse_args()

# 2. Open the file
try:
    fp=open(args.filename, mode="rb")
except:
    logging.critical('Invalid filename: ' + args.filename)
    sys.exit(1)

# 3. Load the config from the file
try:
    config = tomllib.load(fp)
except:
    logging.critical('Invalid TOML content: ' + args.filename)
    sys.exit(1)

# 4. Check if key is declared in a table
key_spec = args.key.split('.')
if len(key_spec) == 1:
    table = config
    key = key_spec[0]
elif len(key_spec) == 2:
    table = config[key_spec[0]]
    key = key_spec[1]
else:
    logging.critical('Invalid key: ' + args.key)
    sys.exit(1)

# 5. Print value. Dont do anything is key does not exist
# TODO: implement an option to raise an error if key does not exit
if key in table :
    print(table[key])

sys.exit(0)