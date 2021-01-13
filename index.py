"""
import librairies
"""
import urllib.request
from bs4 import BeautifulSoup
from openpyxl import Workbook

URL_PAGE = 'http://quotes.toscrape.com/'
page = urllib.request.urlopen(URL_PAGE)
soup = BeautifulSoup(page, 'html.parser')
wb = Workbook()
"""
variables globales
"""
Table = []
all_quote = soup.find_all('div', class_="quote")


def ecrire_dans_fichier_md():
    """
        cette fonction permet d'écrire dans un fichier Markdown
    """
    fichier = open('resultats/quotes/quote.md', "w")
    fichier.writelines("# Citation | Author | Tags\n")
    fichier.writelines("# ---| --- | --- \n")
    for quote in all_quote:
        citation = quote.find('span', class_="text")
        author = quote.find('small', class_='author')
        fichier.writelines("#" + citation.contents[0]
                           + "|" + author.contents[0] + "|")
        all_tags = quote.find_all('a', class_='tag')
        for tag in all_tags:
            fichier.writelines(" "+tag.contents[0])
        fichier.writelines("\n\n")
    fichier.writelines("## bye \n")
    fichier.close()


def lire_fichier_md():
    """
        cette fonction lit un fichier mardown
    """
    fichier = open('resultats/quotes/quote.md', "r")
    ligne = fichier.readline()
    ligne = ligne.strip()
    fichier.close()


ecrire_dans_fichier_md()
lire_fichier_md()


def ecrire_dans_fichier_txt():
    """
        cette fonction permet d'écrire dans un fichier texte
    """
    fichier = open('resultats/tags/tags.txt', "w")
    all_tags = soup.find_all('a', class_='tag')
    fichier.writelines("Liste des tags existants \n")
    tags_array_content = []
    tags_array_response = []
    for tag in all_tags:
        tags_array_content += tag
    for elem in tags_array_content:
        if elem not in tags_array_response:
            tags_array_response.append(elem)
    for element in tags_array_response:
        fichier.writelines(element + "\n")

    fichier.writelines('\n')
    fichier.close()


def lire_fichier_txt():
    """
        cette fonction permet de lire un fichier texte
    """
    fichier = open('resultats/quotes/quote.md', "r")
    ligne = fichier.readline()
    ligne = ligne.strip()
    fichier.close()


ecrire_dans_fichier_txt()
lire_fichier_txt()


def get_authors_list():
    """
        cette fonction récupére une liste d'auteur
    """
    all_authors_list = []
    authors_list = []
    all_authors = soup.find_all('small', class_='author')
    for aut in all_authors:
        all_authors_list += aut
    for author in all_authors_list:
        if author not in authors_list:
            authors_list.append(author)
    return authors_list


get_authors_list()


def write_author_details():
    """
        cette fonction ecrit les details de chaques
        auteurs dans un fichier excel
    """
    author_list = get_authors_list()
    work_sheet = wb.active
    work_sheet['A1'] = "Nom de l'auteur"
    work_sheet['B1'] = "Date de naissance"
    work_sheet['C1'] = "Lieu de naissance"
    work_sheet['D1'] = "Citation"
    i = 2
    for auth in author_list:
        aut = auth.string.replace(' ', '-').replace('.', '').replace("é", "e")
        url_page_auth = 'http://quotes.toscrape.com/author/' + aut + '/'
        page_author = urllib.request.urlopen(url_page_auth)
        soup_author = BeautifulSoup(page_author, 'html.parser')
        author_details = soup_author.find('div', class_="author-details")
        author_name = author_details.find('h3', class_="author-title")
        author_born = author_details.find('span', class_="author-born-date")
        auth_b_loc = author_details.find('span', class_="author-born-location")
        author_desc = author_details.find('div', class_="author-description")
        if author_born.contents != []:
            print(author_born.contents[0])
            work_sheet['A'+str(i)] = author_name.contents[0]
            work_sheet['B'+str(i)] = author_born.contents[0]
            work_sheet['C'+str(i)] = auth_b_loc.contents[0]
            work_sheet['D'+str(i)] = author_desc.contents[0]
            i += 1
    wb.save('resultats/authors/authors.xls')


write_author_details()
