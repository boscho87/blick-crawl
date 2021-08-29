## Selectors
Fetch the Data

#### Current Day Page
`https://www.blick.ch/services/webarchiv/`
```python
# posts
posts = response.css('div.flexitem')
# links
posts.css('a.clickable').get()
# relative Url's to the post
posts.css('a.clickable::attr("href")').get()
```

#### Posts
```python
# url
response.url
# page title
response.css("title::text").get()
# catchword
response.css("header .catchword span::text").get()
# article title
response.css("header span.title::text").get()
# article teaser
response.css(".article-lead::text").get()
# author
response.css(".flexitem .pianocontainer + div span::text").get()
# public date
response.css(".article-metadata > div > div::text").get()
# update date
response.css(".article-metadata > div > div + div + div ::text").get().strip()
# text (html)
response.css(".article-body").getall()  # evt. ohne getall umm daten später zu holen (oder html speichern)
# comments (0 = comments  if comments inactive -> is empty)
response.css(".comment-button::text").get()
``` 