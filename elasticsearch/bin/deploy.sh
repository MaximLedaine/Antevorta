#!/bin/bash
echo Starting

cd api
docker build . --tag gcr.io/egimax/scraper
docker push gcr.io/egimax/scraper
# docker run gcr.io/egimax/scraper