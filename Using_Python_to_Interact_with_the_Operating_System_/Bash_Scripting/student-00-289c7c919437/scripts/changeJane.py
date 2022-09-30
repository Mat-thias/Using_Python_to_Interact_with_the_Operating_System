#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as files:
    for file in files:
        oldname = file.strip()
        newname = oldname.replace("jane", "jdoe")

        subprocess.run(["mv", oldname, newname])

    files.close()

