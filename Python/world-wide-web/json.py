#PYTHON JSON#

import json
import json.js

--------------------------------------------------------------------------
##FROM JSON.JS to JSON.PY##

json_string = '''{
dictionary_name:[{
    "key_1" = "value_1",
    "key_2" = "value_2"
},
{
    "key_3" = "value_3",
    "key_4" = "value_4"
}]
}'''
js_data_variable = json.loads(json_string)

with open("file_path") as variable:

for item in data_variable[dictionary_name]:
    yield item["key_name"]
    del item["key_name"]
    print item["key_name"]

---------------------------------------------------------------------------
##FROM JSON.PY TO JSON.JS##

python_dict = {
    "key_1":"value_1"
    "key_2":"value_2"
}

python_data_variable = json.load(python_dict)
with open("file_path",mode="file_obj_mode_type") as variable:
