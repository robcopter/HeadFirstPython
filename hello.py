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
    return "Offer List"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)
