__author__ = 'Kevin'
from bs4 import BeautifulSoup
import random
from tabulate import tabulate
import requests
import time
from datetime import datetime
import numpy as np

critical_node = "priceblock_ourprice"


def download(url):
    r = requests.get(url)
    while r.status_code != 200:
        time.sleep(2)
        r = requests.get(url)
    return r.text


urls = {
    'Ubiquiti WIFI': (
    'http://www.amazon.com/Ubiquiti-Networks-UniFi-Enterprise-System/dp/B004XXMUCQ/ref=sr_1_1?ie=UTF8&qid=1416266008&sr=8-1&keywords=enterprise+wifi',
    '66.8'),
    'Bar Stool': (
    'http://www.amazon.com/gp/product/B000NPTYJA/ref=s9_simh_gw_p201_d0_i1?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=0VWSB8XJ98GFNRSQ25PC&pf_rd_t=101&pf_rd_p=1688200382&pf_rd_i=507846',
    '64.74'),
}

results = []


def scraping():
    for each_link in urls.keys():
        uri = urls[each_link][0]
        target_price = urls[each_link][1]
        html = download(uri)

        soup = BeautifulSoup(html)
        price = soup.find("span", id="priceblock_ourprice")

        if float(target_price) < float(price.contents[0].strip("$")):
            print "sending email, price decrease"

        results.append((each_link, price.contents[0]))

    print tabulate(results)


if __name__ == '__main__':
    starting_time = datetime.now()
    while 1:
        time.sleep(random.randint(5, 50))
        scraping()
        new_time = datetime.now()
        if np.timedelta64(new_time - starting_time, 's') > 60*5:
            starting_time = datetime.now()