#!/usr/bin/python

import os 
import argparse

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help='directory containing nikto result files to parse',
                        action='store', dest='directory', required=True)
    parser.add_argument('-s', '--str', help='the string to search for. e.g.\
                        "Strict-Transport-Security HTTP header is not defined"',
                        action='store', dest='string', required=True)
    args = parser.parse_args()

    # enumerate filenames in the given dir
    try:
        for filename in os.listdir(args.directory):
            # open file handler on the each filename
            with open(filename,'r') as data:
                if args.string in data.read():
                    data.seek(0)
                    for line in data:
                        if line.startswith('Host'):
                            host = line.split(':')[1].strip()
                        if line.startswith('Port'):
                            port = line.split(':')[1].strip()
                    try:
                        print '%s:%s' % (host, port)
                    except UnboundLocalError:
                        pass
    except IOError:
        pass

if __name__ == "__main__":
    main()
