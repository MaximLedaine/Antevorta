FROM python:3.6.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

# ENTRYPOINT ["scrapyrt", "-i", "0.0.0.0"]

EXPOSE 9080
ENTRYPOINT ["scrapyrt", "-p", "9080", "-i", "0.0.0.0"]
# CMD ["scrapyrt"]

