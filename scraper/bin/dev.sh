#!/bin/bash
echo Starting
echo make sure you have a python environment activated
echo run: pip install -r requirements.txt

if [[ ! -d "$scrapyhost" ]]; then 
    export scrapyhost="http://localhost:9080"
    echo 'export scrapyhost="http://localhost:9080"' >> ~/.bashrc
fi

cd ./scrapy
scrapyrt -i 0.0.0.0 &
python ../api/run.py

echo finished