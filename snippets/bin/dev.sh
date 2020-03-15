#!/bin/bash
echo Starting
echo make sure you have a python environment activated
echo run: pip install -r requirements.txt

conda activate analysisenv

jupyter notebook

echo finished