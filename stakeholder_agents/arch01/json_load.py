import json


a_file = open("designer01.json", "r")
json_object = json.load(a_file)
a_file.close()
print(json_object)
