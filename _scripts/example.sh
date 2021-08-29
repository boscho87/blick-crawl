#!/bin/bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
project_dir=$script_dir/..
FILE_NAME=$project_dir/examples/$(date +%x-%H.%M.%S).json


echo "Start Docker"
container_id_es=$(docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.14.0)
container_id_es_splash=$(docker run -d -p 8050:8050 scrapinghub/splash)

echo "Wait for Containers to start"
sleep 12
source $project_dir/venv/bin/activate
scrapy crawl blick -o $FILE_NAME
echo "Stop Docker $container_id_es"
docker stop $container_id_es_splash
docker stop $container_id_es
