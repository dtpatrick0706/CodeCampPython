        ## Web Services: JSON ##

    # JSON represents data as nested "lists and dictionaries"
import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)         # When we get the info back it is a dictionary
print('Name:',info["name"])
print('Hide:', info["email"]["hide"])

import json
input = ''' [
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009"
        "x" : "7"
        "name" : "Chuck"
    }
]'''

info = json.loads(input)        # When we get the info back it is a list
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])