#!/usr/bin/env python

import os
import sys
from mako.template import Template
from mako.lookup import TemplateLookup

"""
Read the file passed as the first argument as a Mako template and render it to stdout
"""
def main():
    # get the path to the template as a cli argument
    p = sys.argv[1]

    # split into directory/filename
    dn = os.path.dirname(p)
    fn = os.path.basename(p)

    # set up the lookup resolver for templates/includes
    lu = TemplateLookup(directories=[dn])

    # read the template and render to stdout
    t = lu.get_template(fn)
    sys.stdout.write(t.render())


if __name__ == '__main__':
    main()
