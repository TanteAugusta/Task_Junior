"""This module provides script for data parsing."""
import requests
from bs4 import BeautifulSoup
import pandas as pd


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}


class Page:

    def __init__(self, url):
        self.url = url

    def parse_data(self):
        try:
            res = requests.get(url=self.url, headers=HEADERS)
            soup = BeautifulSoup(res.text, "html.parser")
            title_ua = soup.find("div", class_="b-post__title").find("h1").text
            title_en = soup.find("div", class_="b-post__origtitle").text
            imdb = soup.find("span", class_="bold").text
            country = soup.find("h2", text="Страна").find_next("a").text
            duration = soup.find("td", itemprop="duration").text
            description = soup.find("div", class_="b-post__description_text").text
            lst_of_data = [title_ua, title_en, imdb, country, duration, description]
            df = pd.DataFrame([lst_of_data], columns=["Title_ua", "Title_en", "IMDB", "Country", "Duration", "Description"])
            df.to_csv('data.csv')
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    page = Page(url='https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html')
    page.parse_data()
