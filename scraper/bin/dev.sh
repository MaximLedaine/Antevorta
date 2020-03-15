#!/bin/bash
echo Starting
echo make sure you have a python environment activated
echo run: pip install -r requirements.txt

cd ./scrapy
scrapyrt -i 0.0.0.0 &
python ../api/run.py

echo finished