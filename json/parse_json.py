import json

with open("json_files/new_json_file.json") as jsonfile:
    data = json.load(jsonfile)
    print(data)



path_to_json = "json_files/example.json"
json = json.load(open(path_to_json))
value = json["ip"]
print(value)
