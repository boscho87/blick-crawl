#!/bin/bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
project_dir=$script_dir/..

cd $project_dir

scrapy crawl blick