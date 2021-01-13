"""import libraries"""
import urllib.request
from bs4 import BeautifulSoup
from openpyxl import Workbook
wb = Workbook()
URL_PAGE = 'http://quotes.toscrape.com/'
page = urllib.request.urlopen(URL_PAGE)
soup = BeautifulSoup(page, 'html.parser')
allQuote = soup.find_all('div', class_="quote")
tag3 = soup.find_all("span")


def ecrire_dans_fichier_md():
    """ecrire un fichier md"""
    fichier = open("resultats/quotes/quote.md", "w")
    fichier.writelines("# Citation | Author | Tags\n")
    fichier.writelines("# -------------- | ------- | ----------- \n")
    for quote in allQuote:
        all_citation = quote.find('span', class_="text")
        all_authors = quote.find('small', class_='author')
        fichier.writelines("# "+all_citation.contents[0]
                           + " | " + all_authors.contents[0]+" | ")
        all_tag = quote.find_all('a', class_='tag')
        for tag in all_tag:
            fichier.writelines(" "+tag.contents[0])
        fichier.writelines("\n")
    fichier.writelines("## bye \n")
    fichier.close()


def lire_fichier_md():
    """lire le fichier md"""
    fichier = open('resultats/quotes/quote.md', "r")
    ligne = fichier.readline()
    ligne = ligne.strip()
    fichier.close()


def ecrire_dans_fichier_txt():
    """ecrire dans un fichier TXT"""
    fichier = open("resultats/tags/tag.txt", "w")
    fichier.writelines("List of Tags : \n")
    all_tag = soup.find_all('a', class_='tag')
    tabletag = []
    tablereptag = []
    for tag in all_tag:
        tabletag += tag
    for element in tabletag:
        if element not in tablereptag:
            tablereptag.append(element)
    for truc in tablereptag:
        fichier.writelines(" - " + truc + " \n")
    fichier.writelines("\n")
    fichier.writelines("bye bye ! ")
    fichier.close()


def lire_fichier_txt():
    """lire le fichier TXT"""
    fichier = open('resultats/tags/tag.txt', "r")
    ligne = fichier.readline()
    ligne = ligne.strip()
    fichier.close()


def ecrire_dans_fichier_xls():
    """ecrire dans un fichier XLS"""
    work_sheet = wb.active
    work_sheet.title = "Authors"
    all_authors = soup.find_all('small', class_='author')
    tableauth = []
    tablerepauth = []
    work_sheet['A1'] = "Nom de l'autheur"
    work_sheet['B1'] = "Date anniversaire"
    work_sheet['C1'] = "Lieu de naissance"
    work_sheet['D1'] = "Informations"
    i = 2
    for auth in all_authors:
        tableauth += auth
    for aut in tableauth:
        if aut not in tablerepauth:
            tablerepauth.append(aut)
            auto = aut.string
            aut = auto.replace(' ', '-').replace('.', '').replace('é', 'e')
            urlauth = 'http://quotes.toscrape.com/author/'+aut+'/'
            pageauth = urllib.request.urlopen(urlauth)
            soupauth = BeautifulSoup(pageauth, 'html.parser')
            authorname = soupauth.find('h3', class_='author-title')
            authorborndate = soupauth.find('span', class_="author-born-date")
            authcity = soupauth.find('span', class_="author-born-location")
            authordesc = soupauth.find('div', class_="author-description")
            if authorborndate.contents != []:
                work_sheet['A'+str(i)] = authorname.contents[0]
                work_sheet['B'+str(i)] = authorborndate.contents[0]
                work_sheet['C'+str(i)] = authcity.contents[0]
                work_sheet['D'+str(i)] = authordesc.contents[0]
                i += 1
    wb.save('resultats/authors/authors.xlsx')


ecrire_dans_fichier_md()
lire_fichier_md()
ecrire_dans_fichier_txt()
lire_fichier_txt()
ecrire_dans_fichier_xls()
