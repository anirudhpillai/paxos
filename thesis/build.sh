#!/bin/sh

# Build the thesis.
xelatex thesis
bibtex thesis
xelatex thesis
xelatex thesis
