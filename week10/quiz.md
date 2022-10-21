1. Scrape CBS news https://www.cbsnews.com/latest/rss/main and get the following data
    - Title
    - Link
    - Image
    - description


    Using SqlAlchemy create a table called `cbs_news` and insert the data into the table.

    Implement one route called `/cbs_news` that returns the data in json format.


**NOTE**: Use lxml to parse the xml data.