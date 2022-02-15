import requests
from bs4 import BeautifulSoup as BS

def anekdot():
    r = requests.get("https://nekdo.ru/random/")
    html = BS(r.content, "html.parser")
    for el in html.select(".content > .text"):
            res = el
    joke = res.text
    return joke
