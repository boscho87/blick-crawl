#!/bin/bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
project_dir=$script_dir/..


FILE_NAME=$project_dir/examples/$(date +%x-%H.%M.%S).json
echo $FILE_NAME
scrapy crawl blick -o $FILE_NAME