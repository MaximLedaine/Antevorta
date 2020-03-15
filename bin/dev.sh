#!/bin/bash
echo Starting

cd ./scraper
docker-compose up --build -d

cd ../mongodb
docker-compose up --build -d

cd ../elasticsearch
docker-compose up --build -d

echo finished
