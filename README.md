# LDS General Conference Talk Scraper

- For those interested in analyzing semantic trends in official LDS teachings. 
- Requires python 3 and scrapy package.

```
pip3 install scrapy
git clone https://github.com/th3o6a1d/conf_scraper.git
cd conf_scraper
python3 scraper.py
```

- Output will be saved as `talks.csv`. 
- Fields collected: title, author, year, month, text
- With current settings, takes a few hours.
- Refer to scrapy documentation to adjust download speed. 
- Download delay is set to "2" in order to be gentle 
