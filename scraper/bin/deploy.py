#!/usr/bin/python
import os
print('Starting')

os.chdir('api')
os.system("docker build . --tag gcr.io/egimax/scraper")
os.system("docker push gcr.io/egimax/scraper")
# os.system("docker run gcr.io/egimax/scraper")

os.chdir('../scrapy')
os.system("docker build . --tag gcr.io/egimax/scrapy")
os.system("docker push gcr.io/egimax/scrapy")
# os.system("docker run gcr.io/egimax/scrapy")