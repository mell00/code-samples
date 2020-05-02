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

#Navigation by contents() (list of all children of said tag name):



#Navigation by children() (iterable sequence of all children of said tag name):

#Navigation by descendants() ():

#Navigation by string() ():

#Navigation by strings() ():

#Navigation by stripped_strings() ():

#Navigation by parent() ():

#Navigation by parents() ():

#Navigation by next_sibling() ():

#Navigation by next_siblings() ():

#Navigation by previous_sibling() ():

#Navigation by previous_siblings() ():

#Navigation by next_element() ():

#Navigation by next_elements() ():

#Navigation by previous_element() ():

#Navigation by previous_elements() ():
