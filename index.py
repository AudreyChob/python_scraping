# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import os.path

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



Table = []

# for quote in allQuote:
#     allCitation = quote.find_all('span', class_='text')
#     for citation in allCitation:
#         Table += citation.contents

#     allAuthors = quote.find_all('small', class_="author")
#     for author in allAuthors:
#         Table += author.contents
#     allTags = quote.find_all('a', class_='tag')
#     for tag in allTags:
#         Table += tag.contents


# for author in allAuthors:
#     #print(author.string)


# for tag in allTags:
#     #print(tag.string)

#print(Table)



# Contenu = """# Citation|Authors|Tags  
# # --------|--------|--------
# # `Table` |  a | %
# # 4 |  a | %
# # 4 |  a | %
# """

# f = open('quotes/quotes.md','w')
# f.writelines(" Citation|Authors|Tags\n")
# f.writelines(" --------|-------|----\n")

# f.writelines(" `Table`|`Table`|`Table`\n")


allQuote = soup.find_all('div', class_="quote")
tag3 = soup.find_all("span")


# ecrire dans un fichier
def ecrireDansFichierMD(path):
        truc = 'machin'
        fichier = open('quotes\quote.md',"w")
        fichier.writelines("# Citation | Author | Tags\n"  )
        fichier.writelines("# ------------------------------------------------------------------------- | ----------------------- | -------------------------------------- \n"  )
        #print(allQuote)
        for quote in allQuote:
            citation = quote.find('span', class_="text")
            author = quote.find('small', class_='author')
            fichier.writelines("# "+ citation.contents[0]+" | "+author.contents[0]+" | ")
            allTags = quote.find_all('a', class_='tag')
            for tag in allTags:
                fichier.writelines(" "+tag.contents[0])
            fichier.writelines("\n\n")
        fichier.writelines("## bye \n"  )
        fichier.close()
 
# lire un fichier
def lireFichierMD(path):
        fichier = open('quotes\quote.md',"r")
        ligne = fichier.readline()
        ligne = ligne.strip()
        #print(ligne)
        #return ligne
        fichier.close()
 
 
ecrireDansFichierMD("quote.md")
lireFichierMD("quote.md")

def ecrireDansFichierTXT(path):
        truc = 'machin'
        fichier = open('tags/tags.txt',"w")
        allTags = soup.find_all('a', class_='tag')
        print(allTags)
        fichier.writelines("TOUS LES TAGS \n" )
        for tag in allTags:
            tagsArray = []
            for t in tagsArray:
                if t not in tagsArray:
                    tagsArray += t
                    print(tagsArray)
            fichier.writelines(tag.contents[0] + '\n')
        # fichier.writelines("# ------------------------------------------------------------------------- | ----------------------- | -------------------------------------- \n"  )
        # #print(allQuote)
        # for quote in allQuote:
        #     citation = quote.find('span', class_="text")
        #     author = quote.find('small', class_='author')
        #     fichier.writelines("# "+ citation.contents[0]+" | "+author.contents[0]+" | ")
        #     allTags = quote.find_all('a', class_='tag')
        #     for tag in allTags:
        #         fichier.writelines(" "+tag.contents[0])
        #     fichier.writelines("\n\n")
        # fichier.writelines("## bye \n"  )
        fichier.close()

def lireFichierTXT(path):
    fichier = open('quotes\quote.md',"r")
    ligne = fichier.readline()
    ligne = ligne.strip()
    print(ligne)
    #return ligne
    fichier.close()

ecrireDansFichierTXT("tags.txt")
lireFichierTXT("tags.txt")