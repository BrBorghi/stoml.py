# stoml.py - Simple TOML parser (Python 3)

## Name

stoml - writes on standard output the value of a key specified in a TOML file

## Usage

#### Synopsis
stoml [-h] [-V] filename key

stoml [-h] [-V] filename table.key


#### Positional arguments
 - filename:      TOML file
 - key:           get value for key
 - table.key:           get value for key in table

#### Options
 - -h, --help:     show this help message and exit
 -  -V, --Version:  show current version

## Examples

The main usage is to get a value in a TOML file to set an environment variable.

To get the value for `my_key` from a file called `my_file.toml` and set it as a shell environment variable, run
```Shell
export VALUE=`stoml my_file.toml my_key`
```

## Limitations

Currently (release 0.1.0), only a subset of TOML is supported (a most useful subset hopefully).
- _Quoted keys_ are NOT supported
- Only one level of _Dotted keys/Table_ is supported. For instance, _fruit.apple_ is OK, _fruit.apple.color_ is NOT supported (soon to come)
## Requirements
* tomllib - standard in Python 3.11 and higher - otherwise, needs to be installed with `pip install`

## Installation

_(Supposing that Python 3 and tomllib are already installed...)_

- Download `stoml.py` (one file)
- Run
```Shell
chmod a+x stoml.py
mv stoml.py /usr/local/bin/stoml
```

## Rationale

[TOML—Tom’s Obvious Minimal Language](https://toml.io/)—is a configuration file format that 
[is increasingly popular in the Python community](https://realpython.com/python-toml/).

In production environment, it may be useful to share configuration files between shellscripts and Python programs.
_TOML_ is a good candidate. An alternative could be `.env` files.

## Credits

The idea of _stoml_ first appeared in  [freshautomations/stoml](https://github.com/freshautomations/stoml) and was implemented in Go language.
_stoml.py_ is an implementation in python3, easier and safer to install on macos.
