# -*- coding:utf-8 -*-
# !/usr/bin/python3


from requests_html import HTMLSession
import bs4



def demo():
    session = HTMLSession()

    resp = session.get('https://china.nba.com/news/')
    resp.html.render()
    bsobj = bs4.BeautifulSoup(resp.html.html, 'html.parser')
    wraps = bsobj.findAll(name='div', attrs={"class": "news-wrap"})

    for wrap in wraps:
        links = wrap.findAll('a')
        for link in links:
            url = link.get('href')
            print(url)



demo()
