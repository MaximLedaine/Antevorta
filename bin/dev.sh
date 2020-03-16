#!/bin/bash
echo Starting

cd ./scraper
docker-compose up --build -d

cd ../api
docker-compose up --build -d

cd ../ui
npm run serve

echo finished
