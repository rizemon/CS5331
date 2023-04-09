#!/usr/bin/env python3
import os.path as path
import re
from distutils.util import strtobool


class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        # extract the file name from __file__. __file__ is proxymodules/name.py
        self.name = path.splitext(path.basename(__file__))[0]
        self.description = 'Protects a web server from request smuggling attacks'
        self.verbose = verbose
        self.source = None
        self.destination = None
        self.incoming = incoming
        if options is not None:
            if 'verbose' in options.keys():
                self.verbose = bool(strtobool(options['verbose']))

    def execute(self, data):
        matches = re.findall(rb"HTTP/1.1\r\n", data)

        if self.verbose:
            print(matches)

        if len(matches) > 1:
            print("Request Smuggling Detected!")
            return b"GET /404 HTTP/1.1\r\n\r\n"

        return data

    def help(self):
        h = '\tverbose: override the global verbosity setting'
        return h


if __name__ == '__main__':
    print('This module is not supposed to be executed alone!')

