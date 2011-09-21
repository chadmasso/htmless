#!/usr/bin/python
import sys, re, os
from jinja2 import FileSystemLoader, Environment

dest_path = '../'
htmless_file = sys.argv[1]
env = Environment(loader=FileSystemLoader(os.path.dirname(htmless_file)))
file_name = os.path.basename(htmless_file)
template = env.get_template(file_name)
result = template.render()
dest = os.path.splitext(file_name)[0]

destination = open(dest_path + dest + '.html', 'w')
destination.write(result)
destination.close()

print "Compiled and Saved"