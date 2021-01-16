#!/bin/bash

# Exit on error
set -e

echo "Setting up project"

conda env create -f environment.yml
