#PYTHON URLLIB#

import tempfile
import shutil
import urllib.request

#Basic URL fetching:
with urllib.request.urlopen("url_address") as response:
    html = response.read()

#Copy resource via URL and store in a temporary location (named tmp_file):
with urllib.request.urlopen("url_address") as response:
    with tempfile.NamedTemporaryFile(delete=true/false) as tmp_file:
        shutil.copyfileobj(response,tmp_file)
    with open(tmp_file.name) as html:
        pass
