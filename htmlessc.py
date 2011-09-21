#!/usr/bin/python
import sys, re, os
from jinja2 import FileSystemLoader, Environment

dest_path = '../'
htmless_file = sys.argv[1]
env = Environment(loader=FileSystemLoader(os.path.dirname(htmless_file)))
template = env.get_template(os.path.basename(htmless_file))
result = template.render()
dest = os.path.basename(htmless_file)[0:os.path.basename(htmless_file).index('.htmless')]

destination = open(dest_path + dest + '.html', 'w')
destination.write(result)
destination.close()

print "Compiled and Saved"

         


