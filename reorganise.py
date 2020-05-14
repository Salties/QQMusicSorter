#!/usr/bin/python3

import os
import sys
import tqdm
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
if target in artistlist:
    print("INFO: Target already folder exist.")
    artistlist.remove(target)

for artist in tqdm.tqdm(artistlist):
    if os.path.isdir(artist):
        cmd  = "rsync -r ./'{}'/* {}".format(artist, target)
        print("Executing: [{}]".format(cmd))
        os.system(cmd)
