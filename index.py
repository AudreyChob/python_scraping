
from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage = 'http://quotes.toscrape.com/'
page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')
put = False
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
 
ecrireDansFichierMD("quote.md")
lireFichierMD("quote.md")
ecrireDansFichierTXT("tag.txt")
lireFichierTXT("tag.txt")















# Table = []

# for quote in allQuote:
#         Table += allCitation.contents
#         Table += allAuthors.contents
        # allTags = quote.find_all('a', class_='tag')
        # for tag in allTags:
        #     Table += tag.contents



# for author in allAuthors:
#     #print(author.string)


# for tag in allTags:
#     #print(tag.string)

#print(Table)