#!/bin/bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
project_dir=$script_dir/..
FILE_NAME=$project_dir/examples/$(date +%x-%H.%M.%S).json
source $project_dir/venv/bin/activate
scrapy crawl blick -o $FILE_NAME