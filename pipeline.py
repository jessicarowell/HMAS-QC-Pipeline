#!/usr/bin/env python

import logging, sys, os, argparse, shutil
import mpy_batch, config_checker

# Parse user arguments (which specify the config file)
if len(sys.argv) < 2:
    print('You forgot to specify your config file!')
    sys.exit(1)

parser = argparse.ArgumentParser(description = 'Run in batch mode or run a single sample.')
parser.add_argument('-c', '--config', metavar = '', help = 'Specify configuration file')

args = parser.parse_args() # yields a Namespace object

# Send the specified config file to the config_checker program
# Run the config_checker program and return
configFile = config_checker.main()


# Check that the input files exist
def checkFile(filename):
    try: 
        f = open(filename)
        f.close()
    except FileNotFoundError:
        print('File not found, did you remember to create it?')

# Also check the batch file - will need to import the name here somehow
checkFile(oligosfile)

# Check explicitly that Mothur is on the path (mothur_py will also check)
# Probably want to do this in a nicer way - when I update the other checks
def find_tool(name):
    return shutil.which(name) is not None

if find_tool("mothur") == False:
        print('{0} not found on path. Is it installed?'.format(name), sys.stderr)
        sys.exit(1)

# Import Mothur
try:
    from mothur_py import Mothur
    m = Mothur()
except:
    print("Unable to import mothur_py module.  Is it installed and on the path?")
    print("Program exited because mothur_py could not be imported", sys.stderr)
    sys.exit(1)
    
#### Set directories for the raw files (mothur_py should dump intermediate files in the current folder?)
    # Decide how to work out the directories

mpy_batch.main(configFile)
    

