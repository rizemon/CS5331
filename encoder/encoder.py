import os.path as path
import re
from distutils.util import strtobool
import base64

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
        length = 0
        x = data.split(b'\r\n\r\n')
        headers = x[0]
        body = x[1]
        if body:
            body = base64.b64encode(body)
            length = len(body)
        
        headers = re.sub(b".*Content-Length: \d+", b"Content-Length: " + str(length).encode(), headers)
        request = headers + b'\r\n\r\n' + body + b'\r\n'

        return request

    def help(self):
        h = '\tverbose: override the global verbosity setting'
        return h


if __name__ == '__main__':
    print('This module is not supposed to be executed alone!')