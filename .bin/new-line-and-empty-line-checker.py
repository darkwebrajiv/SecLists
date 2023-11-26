#!/usr/bin/env python3

# test string: ./.bin/new-line-checker.py "Fuzzing/file-extensions-all-cases.txt Fuzzing/file-extensions-lower-case.txt Fuzzing/file-extensions-upper-case.txt Fuzzing/file-extensions.txt"

import os
import sys

print("[+] New line check")

if not sys.argv[1]:
    exit(0)

files=sys.argv[1].split(" ")

for i in files:
    if not os.path.isfile(i):
        print("[!] %s does not exist!"%(i))
        exit(2)

pass_status=True

for i in files:
    contents=open(i,"rb").read()

    if contents[-1] == b'\n':
        print("[!] Error: %s ends with a new line!"%(i))
        pass_status=False
        
    print("[+] %s passed new line check!"%(i))

    counter=1

    for line in contents.split(b'\n'):
        if len(line)==0:
            print("[!] Error: %s has an empty entry at line %i!"%(i,counter))
            pass_status=False

        counter+=1
    print("[+] %s passed empty line check!"%(i))

if pass_status:
    print("[+] All files passed checks")
    exit(0)

print("[!] Error: One or more files failed to pass the checks")
exit(2)
