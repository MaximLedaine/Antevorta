#!/bin/bash
echo Starting

# if [[ ! -d "$scrapyhost" ]]; then 
#     export scrapyhost="http://localhost:9080"
#     echo 'export scrapyhost="http://localhost:9080"' >> ~/.bashrc
# fi

docker network create es-net
docker run --name elasticsearch -d --net es-net -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e="xpack.monitoring.collection.enabled=true" elasticsearch:7.3.1
docker run --name kibana -d --net es-net -p 5601:5601 kibana:7.3.1
nodemon ./app.js localhost 4100

docker stop elasticsearch
docker rm elasticsearch -f

docker stop kibana
docker rm kibana -f

docker network rm es-net

echo finished


