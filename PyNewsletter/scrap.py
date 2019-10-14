# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:15:31 2019
@author: Sarvesh
"""
import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def scrappy():
    my_url = 'https://timesofindia.indiatimes.com/'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    Author = '  Created by Sarvesh,Onkar,Eeshani,Fauzia  '
    filename="news.txt"
    f=open(filename,'w',encoding="utf-8")
    
    page_soup = soup(page_html, "html.parser")
    print(page_soup.p.text)
    print("\n\n\n")
    f.write(page_soup.p.text + "\n\n\n" )
    containers = page_soup.find_all("div", {"class": "top-story"})

    container = containers[0]
    contain = container.ul
    cont = contain.find_all("li")
    con = cont[0]
    top = container.h2.text
    top_n = top.center(80, '#')
    print(top_n)
    print('\n')
    f.write(top_n + '\n')
    for con in cont:
        title = con.a["title"]
        link = con.a["href"]
        print(title)
        if link[0] == '/':
            print(my_url+link[1:])
            f.write(title + '\t' + my_url+link[1:] + "\n")
        else:
            print(link)
            f.write(title + '\t' + link + "\n")
        print('\n')


    top = page_soup.find("div", {"class": "sechead"})
    top_n = top.a.text.center(80, '#')
    print(top_n)
    containers = page_soup.find_all("div", {"class": "latestNewContainer"})
    container = containers[0]
    contain = container.ul
    cont = contain.find_all("li")
    con = cont[0]
    print('\n')
    for con in cont:
        title = con.a["title"]
        link = con.a["href"]
        print(title)
        if link[0] == '/':
            print(my_url+link[1:])
            f.write(title + '\t' + my_url+link[1:] + "\n")
        else:
            print(link)
            f.write(title + '\t' + link + "\n")
        print('\n')

    f.close()
    print('#'*80)
    print(Author.center(80, '$'))
    print('\n\n')
