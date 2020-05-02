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

            #Access the comment object itself:
            type(comment)
            ##<class 'bs4.element.Comment'>##

            #Display the comment object with HTML formatting:
            print(soup.b.prettify())
            ##<b>##
            ##<!--comment-->##
            ##</b>##

        #Create and access a Stylesheet object (special type of navigable string for embedded CSS documents)
        markup = "<style><!--stylesheet_name.css--></style>"
        soup = BeautifulSoup(markup)
        stylesheet = soup.b.string
        type(stylesheet)
        ##<class 'bs4.element.Stylesheet'>##

        #Create and access Script object (special type of navigable string for embedded JS documents)
        markup = "<script><!--script_name.js--></script>"
        soup = BeautifulSoup(markup)
        script = soup.b.string
        type(script)
        ##<class 'bs4.element.Script'>##

        #Create and access TemplateString object (special type of navigable string for embedded HTML templates)
        markup = "<template><!--temp_name.html--></template>"
        soup = BeautifulSoup(markup)
        templstr = soup.b.string
        type(template)
        ##<class 'bs4.element.TemplateString'>##


    #BeautifulSoup object
        #Represent whole parsed document:
        with open("index.html") as fp:
            soup = BeautifulSoup(fp)

        soup = BeautifulSoup("<html>data</html>")

        #Combine two parsed documents:
        doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
        footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
        doc.find(text="INSERT FOOTER HERE").replace_with(footer)
        ##u'INSERT FOOTER HERE'##
        print(doc)
        ##<?xml version="1.0" encoding="utf-8"?>##
        ##<document><content/><footer>Here's the footer</footer></document>##
