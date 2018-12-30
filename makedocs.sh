#!/bin/bash
# Remake the documentation for campy.

# Print all of the commands that are being run
set -x

OLD_DIR=$(pwd)
# Move to the top-level of the project.
cd $(git rev-parse --show-toplevel)
cd docs-src
make html
cp -r docs-src/_build/html/ docs/
cd "${OLD_DIR}"
set +x