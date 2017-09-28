#!/usr/bin/env python
#A system Information Gathering Script
import subprocess

#Command 1
def uname_func(): 

    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information whit %s command:\n" % uname
    subprocess.call([uname,uname_arg])
#subprocess.call(["uname -a", shell = True])

#Command 2
def disk_func():

    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering diskspace information %s command:\n" % diskspace
    subprocess.call([diskspace,diskspace_arg])

#Main fuction that call other functions
def main():
    uname_func()
    disk_func()

main()
