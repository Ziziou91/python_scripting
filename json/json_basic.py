import json

car_data = {
    "name": "tesla",
    "engine": "electric",
    "reliability": None
}

# json.dumps() --> serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(type(car_data_json_string))

# json.dump() --> Create a string object and expects a file object to write to
with open("json_files/new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)