#!/usr/bin/env python
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

def patch_router_controller(before):
    regex = r"x-swagger-router-controller: \"(\w*)\.\.(\w*)\""
    subst = 'x-swagger-router-controller: "\\1.\\2"'

    # You can manually specify the number of replacements by changing the 4th argument
    after = re.sub(regex, subst, before, 0)

    return after

def main(argv):
    swagger_yaml = argv[0]

    before = ''
    with open(swagger_yaml) as rfile:
        before = rfile.read()

    # You can manually specify the number of replacements by changing the 4th argument
    after = patch_router_controller(before)

    with open(swagger_yaml, 'w') as wfile:
        wfile.write(after)

    return 0

if __name__ == "__main__":
    # execute only if run as a script
    import sys
    sys.exit(main(sys.argv[1:]))
