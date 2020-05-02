##PYTHON HTML PROCESSING SUPPORT##

import html

#Convert string of Unicode characters into HTML-safe sequence:
string = "string"
html.escape(string.quote=True)

#Convert string of HTML5 character references into Unicode characters:
string = "string"
html.unescape(string)

##HTMLParser##

    #
    html.parser.HTMLParser
