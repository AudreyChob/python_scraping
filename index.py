
from bs4 import BeautifulSoup
import urllib.request
import csv

from openpyxl import Workbook

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
# allCitation = soup.find_all('span', class_="text")
# allAuthors = soup.find('small', class_='author')
#allTags = soup.find_all('a', class_='tag')
 
# ecrire dans un fichier
def ecrireDansFichierMD(path):
        fichier = open('quotes\quote.md',"w")
        fichier.writelines("# Citation | Author | Tags\n"  )
        fichier.writelines("# ------------------------------------------------------------------------- | ----------------------- | -------------------------------------- \n"  )
        for quote in allQuote:
                allCitation = quote.find('span', class_="text")
                allAuthors = quote.find('small', class_='author')
                fichier.writelines("# "+allCitation.contents[0]+" | "+allAuthors.contents[0]+" | ")
                allTags = quote.find_all('a', class_='tag')
                for tag in allTags:
                        fichier.writelines(" "+tag.contents[0])
                fichier.writelines("\n")
        fichier.writelines("## bye \n"  )
        fichier.close()

def lireFichierMD(path):
        fichier = open('quotes\quote.md',"r")
        ligne = fichier.readline()
        ligne = ligne.strip()
        fichier.close() 
    

def ecrireDansFichierTXT(path):
        
        fichier = open("tags/tag.txt","w")
        fichier.writelines("List of Tags : \n"  )
        allTags = soup.find_all('a', class_='tag')
        tabletag = []  
        tablereptag = []
        for tag in allTags:
                tabletag += tag
        for element in tabletag:
                if element not in tablereptag:
                        tablereptag.append(element)    
        for truc in tablereptag:
                fichier.writelines(" - "+truc+ " \n")                
        fichier.writelines("\n")
        fichier.writelines("bye bye ! ")
        fichier.close()
           
def lireFichierTXT(path):
        fichier = open('tags/tag.txt',"r")
        ligne = fichier.readline()
        ligne = ligne.strip()
        fichier.close()

def ecrireDansFichierXLS(path):  
        # fichier = open("tags/tag.txt","w")
        allAuthors = soup.find_all('small', class_='author')
        tableauth = []  
        tablerepauth = []
        for auth in allAuthors:
                tableauth += auth
        for auto in tableauth:
                if auto not in tablerepauth:
                        tablerepauth.append(auto) 
                        auto = auto.string.replace(' ', '-').replace('.', '').replace('é', 'e').replace('è', 'e')
                        urlauth = 'http://quotes.toscrape.com/author/'+auto+'/'
                        pageauth = urllib.request.urlopen(urlauth)
                        soupauth = BeautifulSoup(pageauth, 'html.parser')  
                        authorname = soupauth.find('h3', class_='author-title')
                        authorborndate = soupauth.find('span', class_="author-born-date")
                        authorborncity = soupauth.find('span', class_="author-born-location")
                        authordesc = soupauth.find('div', class_="author-description")
                        if authorborndate.contents != []:
                                print(authorname.contents[0])
                                print(authorborndate.contents[0])
                                print(authorborncity.contents[0])
                                print(authordesc.contents[0])

             

        

        # fichier.writelines("bye bye ! ")
        # fichier.close()
           
# def lireFichierXLS(path):
#         fichier = open('tags/tag.txt',"r")
#         ligne = fichier.readline()
#         ligne = ligne.strip()
#         fichier.close()
 
ecrireDansFichierMD("quote.md")
lireFichierMD("quote.md")
ecrireDansFichierTXT("tag.txt")
lireFichierTXT("tag.txt")
ecrireDansFichierXLS('truc')

