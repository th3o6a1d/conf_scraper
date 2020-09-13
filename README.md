# LDS General Conference Talk Scraper

Requires python 3 and scrapy package.

```
pip3 install scrapy
python3 scraper.py
```

- Output will be saved as `talks.json`. 
- With current settings, takes 
- Sample Output: 

```
{"title": "The Cause Is Just and Worthy", "author": "Spencer W. Kimball", "year": "1974", "month": "04", "text": "Now, beloved brethren and sisters...In the name of our Lord Jesus Christ. Amen."},

```

- Refer to scrapy documentation to adjust download speed. 
- Download delay is set to "2" in order to be gentle 
