#!/usr/bin/env python

import sys
from mako.template import Template
from mako.lookup import TemplateLookup

"""
Read stdin as a Mako template and render it to stdout
"""
def main():
    lu = TemplateLookup(directories=['in'])
    t = lu.get_template(sys.argv[1])
    sys.stdout.write(t.render())

if __name__ == '__main__':
    main()
