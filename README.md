# Blick Analyzer

This Project fetches Data from https://www.blick.ch to analyze it. It's a "Lab" Project about Big-Data

### Crawler
Fetch Posts from Blick.ch and stores it in a Database (Not Yet Implemented)
One data Fetch has the Size of +/- 400KB, when we fetch every Day 24 Times, this will be 3G Data after one year

#### How to Crawl

##### Setup
TBD

Install scrapy https://scrapy.org in your `project-dir/venv`

run:  
- example: `./_scripts/example.sh`
- run `scrapy crawl blick` 



### Analyzer
- Not yet Implemented

### Roadmap
- Implement the Crawler, store the Date (not public)
- Update the features (attributes, to fetch)
- Create a config file for the Database
- Implement a healthcheck (so we don't loose data)
- Implement a Analyzer, so we can Visualize the fetched Data

&copy; [boscho87 - Simon D. Mueller](https://github.com/boscho87)
