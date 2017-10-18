#!/usr/bin/env python3

import argparse
import os
import color

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--recursive', action='store_true')
args = parser.parse_args()

def getPathFiles(path, dirs, files):
    print(color.red(path))
    for dir in dirs:
        print('--', color.blue(dir))
    for file in files:
        print('--', file)
def main():
    cwd = os.getcwd()
    for path, dirs, files in os.walk(cwd):
        if not args.recursive:
            if path == cwd:
                getPathFiles(path, dirs, files)
        else:
            getPathFiles(path, dirs, files)
if __name__ == '__main__':
    main()
