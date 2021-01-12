from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
#print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))
# <html><head></head><body>Sacré bleu!</body></html>

#TAG
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
typetag = type(tag)
#print(typetag)
# <class 'bs4.element.Tag'>

#NOM
tag.name
# 'b'
#print(tag.name)

tag.name = "blockquote"
tag
# <blockquote class="boldest">Extremely bold</blockquote>
#print(tag)

#ATTRIBUTS
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
tag['id']
# 'boldest'
#print(tag['id'])

tag.attrs
# {'id': 'boldest'}
# print(tag.attrs)

tag['id'] = 'verybold'
tag['another-attribute'] = 1
#print(tag)
# <b another-attribute="1" id="verybold"></b>

del tag['id']
del tag['another-attribute']
#print(tag)
# <b>bold</b>

#print(tag['id'])
# KeyError: 'id'
#print(tag.get('id'))
# None

#Attribut a valeur multiple
css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
#print(css_soup.p['class'])
# ['body']

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
#print(css_soup.p['class'])
# ['body', 'strikeout']

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
#print(id_soup.p['id'])
# 'my id'

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
#print(rel_soup.a['rel'])
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
#print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>

no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
#print(no_list_soup.p['class'])
# 'body strikeout'


#print(id_soup.p.get_attribute_list('id'))
# ["my id"]

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
#print(xml_soup.p['class'])
# 'body strikeout'

class_is_multi= { '*' : 'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
#print(xml_soup.p['class'])
# ['body', 'strikeout']

from bs4.builder import builder_registry
builder_registry.lookup('html').DEFAULT_CDATA_LIST_ATTRIBUTES

#NavigableString
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
#print(tag.string)
# 'Extremely bold'
#print(type(tag.string))
# <class 'bs4.element.NavigableString'>


unicode_string = str(tag.string)
#print(unicode_string)
# 'Extremely bold'
#print(type(unicode_string))
# <type 'str'>

tag.string.replace_with("No longer bold")
#print(tag)
# <b class="boldest">No longer bold</b>

#BeautifulSoup
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# 'INSERT FOOTER HERE'
#print(doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>

#print(soup.name)
# '[document]'

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
#print(type(comment))
# <class 'bs4.element.Comment'>

#print(comment)
# 'Hey, buddy. Want to buy a used parser'

#print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>

from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)

print(soup.b.prettify())
# <b>
#  <![CDATA[A CDATA block]]>
# </b>