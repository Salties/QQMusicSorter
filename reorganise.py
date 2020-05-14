#!/usr/bin/python3

import os
import sys
import subprocess

if len(sys.argv) < 2:
    print("No target")
    exit()

# Create target folder
target=sys.argv[1]
try:
    os.makedirs(target, exist_ok = True)
except OSError as err:
    print(err)
    exit()

# Get list of artists.
artistlist = os.listdir()

for artist in artistlist:
    if os.path.isdir(artist):
        cmd = "cp -rf ./'{}'/* {}".format(artist, target)
        os.system(cmd)
