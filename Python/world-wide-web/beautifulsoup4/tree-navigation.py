##BEAUTIFULSOUP4 TREE NAVIGATION##

<head><title>.</title></head>
<a href=https://www.google.com/>Google</a>
<a href=https:https://github.com/>GitHub</a>
----------------------------------------------
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#Navigation by tag name (more specifically, the first tagline with said tag name):
soup.tag_name

    #ex1:
    soup.head
    ##<head><title>.</title></head>##

    #ex2:
    soup.title
    ##<title>.</title>##

    #Chained tag names:
    soup.head.title
    ##<title>.</title>##

#Navigation by find_all() (all taglines with said tag name):
soup.find_all('tag_name')

    #ex:
    soup.find_all('a')
    ##<a href=https://www.google.com/>Google</a><a href=https:https://github.com/>GitHub</a>##
