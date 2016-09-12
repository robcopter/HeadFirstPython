import os
import json
import urllib2
from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, render_template, send_from_directory
app = Flask(__name__)


@app.route("/")
def indexPage():
    return render_template('index.html')

@app.route("/about")
def aboutPage():
    return render_template('about.html')


@app.route('/templates/<path:path>')
def static_proxy(path):
    return send_from_directory("templates", path)

@app.route("/offer")
def getOffers():
    try:
        paytmPageURL = os.environ.get("JSON_URL_1")
        page = urllib2.urlopen(paytmPageURL).read()
        jsonData = json.loads(page)
        offersJSON = jsonData['homepage_layout'][0]['items']
        paytmOfferList = []
        for offer in offersJSON:
            singleOffer = {}
            fullOfferString = offer['name']
            firstIndex = fullOfferString.find(':')
            secondIndex = fullOfferString.find('#')
            if firstIndex != -1 & secondIndex != -1:
                singleOffer['offerName'] = fullOfferString[secondIndex+1:len(fullOfferString)].strip()
                singleOffer['offerPromoCode'] = fullOfferString[firstIndex+1:secondIndex-1].strip()
            else:
                singleOffer['offerName'] = offer['name']
                singleOffer['offerPromoCode'] = 'NOT AVAILABLE'
            singleOffer['offerURL'] = offer['url']
            paytmOfferList.append(singleOffer)

        redbusPageURL = os.environ.get("REDBUS_OFFER_URL")
        print(redbusPageURL)
        redbusPage = urllib2.urlopen(redbusPageURL)
        redbus_soup = BeautifulSoup(redbusPage, 'html.parser')
        offerBoxes = redbus_soup.select(".offer-box")
        redbusOfferList = []
        for offerBox in offerBoxes:
            singleOffer = {}
            singleOffer['offerName'] = offerBox.find("h2").text
            singleOffer['offerInfo'] = offerBox.find("h3").text
            singleOffer['offerValidTill'] = offerBox.find_all("p")[0].text
            singleOffer['offerPromoCode'] = offerBox.find_all("p")[1].text
            singleOffer['offerURL'] = os.environ.get("REDBUS_OFFER_URL")
            redbusOfferList.append(singleOffer)

        return jsonify(paytm=paytmOfferList, redbus=redbusOfferList, status="OK", message="OK")
    except Exception as e:
        print(e)
        return jsonify(status="EXCEPTION", message=e)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
