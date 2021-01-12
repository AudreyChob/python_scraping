# import libraries
from bs4 import BeautifulSoup
import urllib.request
from openpyxl import Workbook

# #specifier l' url
urlpage = 'http://quotes.toscrape.com/'
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')
wb = Workbook()
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
# tag3 = soup.find_all("span")


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
    fichier = open('tags/tags.txt',"w")
    allTags = soup.find_all('a', class_='tag')
    #print(allTags)
    fichier.writelines("Liste des tags existants \n" )
    tagsArrayContent = []
    tagsArrayResponse = []
    for tag in allTags:
        tagsArrayContent += tag
    for t in tagsArrayContent:
        #print(t)
        if t not in tagsArrayResponse: 
            tagsArrayResponse.append(t)
    for element in tagsArrayResponse:
            fichier.writelines(element + "\n")

    fichier.writelines('\n')
    fichier.close()

def lireFichierTXT(path):
    fichier = open('quotes\quote.md',"r")
    ligne = fichier.readline()
    ligne = ligne.strip()
    fichier.close()

ecrireDansFichierTXT("tags.txt")
lireFichierTXT("tags.txt")

def getAuthorsList(): 
    allAuthorsList = []
    authorsList = []
    allAuthors = soup.find_all('small', class_='author')
    for a in allAuthors:
        allAuthorsList += a
        #print(allAuthorsList)
    for author in allAuthorsList:
        if author not in authorsList:
            authorsList.append(author)
            #print(authorsList)
    return authorsList
        # auteur = author.string.replace(' ', '-')
        # print(auteur)
        # urlpageAuthor = 'http://quotes.toscrape.com/author/'+auteur+'/'
        # pageAuthor = urllib.request.urlopen(urlpageAuthor)
        # soupAuthor = BeautifulSoup(pageAuthor, 'html.parser')
        # #print(soupAuthor)

getAuthorsList()  


def writeAuthorDetails():
    authorList = getAuthorsList()
    #print(authorList)
    for author in authorList:
        auteur = author.string.replace(' ', '-').replace('.','').replace("é", "e").replace("è", "e").replace("ë", "e").replace("ê", "e")
        #print(auteur)
        urlpageAuthor = 'http://quotes.toscrape.com/author/'+auteur+'/'
        pageAuthor = urllib.request.urlopen(urlpageAuthor)
        soupAuthor = BeautifulSoup(pageAuthor, 'html.parser')
        # print(soupAuthor)
        authorDetails = soupAuthor.find('div', class_="author-details")
        # print(authorDetails.contents)
        authorName = authorDetails.find('h3', class_="author-title")
        #print(authorName.contents[0])
        authorBorn = authorDetails.find('span', class_="author-born-date")
        authorBornLocation = authorDetails.find('span', class_="author-born-location")
        authorDescript = authorDetails.find('div', class_="author-description")
        if authorBorn.contents != []:
            print(authorBorn.contents[0])
            print(authorName.contents[0])
            print(authorBornLocation.contents[0])
            print(authorDescript.contents[0])


writeAuthorDetails()

