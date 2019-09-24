#!/bin/bash
echo Starting

cd api
docker build . --tag gcr.io/egimax/scraper
docker push gcr.io/egimax/scraper
# docker run gcr.io/egimax/scraper

cd ../scrapy
docker build . --tag gcr.io/egimax/scrapy
docker push gcr.io/egimax/scrapy
# docker run gcr.io/egimax/scrapy