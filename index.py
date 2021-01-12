# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv


# #specifier l' url
urlpage = 'http://quotes.toscrape.com/'
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')

#print(soup)

# tag = soup.span
# print(tag.string)

# tag = soup.span['class']
# print(tag)


# tag2 = soup.find("span")
# print(tag2.contents[0])

allQuote = soup.find_all('div', class_="quote")

tag3 = soup.find_all("span")
allCitation = soup.find('span', class_="text")
allAuthors = soup.find('small', class_='author')
allTags = soup.find_all('a', class_='tag')

Table = []

for quote in allQuote:
        Table += allCitation.contents
        Table += allAuthors.contents
        allTags = quote.find_all('a', class_='tag')
        for tag in allTags:
            Table += tag.contents



# for author in allAuthors:
#     #print(author.string)


# for tag in allTags:
#     #print(tag.string)

#print(Table)

#!/usr/bin/env python
# -*- coding: UTF8 -*-
 
 
# ecrire dans un fichier
def ecrireDansFichier(path):
        truc = 'machin'
        fichier = open('quotes\quote.md',"w")
        fichier.writelines("# Citation | Author | Tags\n"  )
        fichier.writelines("# ------------------------------------------------------------------------- | ----------------------- | -------------------------------------- \n"  )
        for quote in allQuote:
         fichier.writelines("# "+allCitation.contents[0]+" | "+allAuthors.contents[0]+" | ")
         for tag in allTags:
            fichier.writelines(" "+tag.contents[0])
         fichier.writelines("\n")
        fichier.writelines("## bye \n"  )
        fichier.close()
 
# lire un fichier
def lireFichier(path):
        fichier = open('quotes\quote.md',"r")
        ligne = fichier.readline()
        ligne = ligne.strip()
        #print(ligne)
        #return ligne
        fichier.close()
 
 
ecrireDansFichier("quote.md")
lireFichier("quote.md")