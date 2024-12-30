#!/bin/bash -l
set -e
if [ "$#" -eq 0 ]; then
  exec {{cookiecutter.package_name}} --help
else
  exec "$@"
fi
