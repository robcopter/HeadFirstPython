import os
import json
import urllib2
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "My First Python Scraper!"

@app.route("/offer")
def getOffers():
    pageURL=os.environ.get("JSON_URL_1")
    page = urllib2.urlopen(pageURL).read()
    jsonData=json.loads(page)
    # zero=jsonData['homepage_layout'][0]['items'][0]['name']

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
