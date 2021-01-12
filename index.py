# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import os.path

# #specifier l' url
urlpage = 'http://quotes.toscrape.com/'
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')

print(soup)

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

print(Table)



Contenu = """# Citation|Authors|Tags  
# --------|--------|--------
# `Table` |  a | %
# 4 |  a | %
# 4 |  a | %
"""

f = open('quotes/quotes.md','w')
f.writelines(" Citation|Authors|Tags\n")
f.writelines(" --------|-------|----\n")

f.writelines(" `Table`|`Table`|`Table`\n")

