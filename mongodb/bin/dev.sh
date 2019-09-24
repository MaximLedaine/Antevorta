#!/bin/bash
echo Starting

# if [[ ! -d "$scrapyhost" ]]; then 
#     export scrapyhost="http://localhost:9080"
#     echo 'export scrapyhost="http://localhost:9080"' >> ~/.bashrc
# fi

docker run --rm mongo mongo &
docker run --rm --name mongo-express -p 8081:8081 mongo-express &
node ./app.js

docker stop mongo
docker rm mongo -f

docker stop mongo-express
docker rm mongo-express -f


echo finished