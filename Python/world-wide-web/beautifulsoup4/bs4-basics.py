#BEAUTIFULSOUP4#

from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")

#Tags
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
type(tag)
##<class 'bs4.element.Tag'>##

    #Tag name
        #Return tag name:
        tag.name

        #Return document name:
        soup.name

        #Change tag name:
        tag.name = "blockquote"

    #Single-valued tag attribute(s)
        #Access tag attribute:
        tag['attr']

        #Change tag attribute value:
        tag['attr'] = new_attr_value

        #Delete attribute:
        del tag['attr']

        #Access dictionary of tag attribute(s):
        tag.attrs

    #Multi-valued tag attribute(s):
        soup = BeautifulSoup('<p class=val1 val2></p>')
        soup.p['class']
        ##[val1,val2]##

        soup=BeautifulSoup('<p class=val1 val2></p>','html',multi_valued_attributes=None)
        soup.p['class']
        ##[val1 val2]##

    #Navigable string
        #Access text stored within tag:
        tag.string

        #Access text stored within tag, converted to Python Unicode:
        unicode(tag.string)

        #Replace existing text string stored within tag with another:
        tag.string.replace_with("new_string")

        #Comment object (special type of navigable string)
            #Create a comment object:
            markup = "<b><!--comment--></b>"
            soup = BeautifulSoup(markup)
            comment = soup.b.string

    #BeautifulSoup object
        #Represent whole parsed document:
        with open("index.html") as fp:
            soup = BeautifulSoup(fp)

        soup = BeautifulSoup("<html>data</html>")
