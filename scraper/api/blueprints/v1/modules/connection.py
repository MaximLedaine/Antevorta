import os

url = os.environ.get('scrapyhost') if os.environ.get('scrapyhost') else 'http://localhost:9080'