import sys
import os
import json
import yaml


def load_json(file_name) -> dict:
    if os.path.exists(file_name):
        file = open(file_name, "r")
        data = json.load(file)
        file.close()
        print("JSON is valid.")
        return data
    else:
        print(f"no file found with name {file_name}")


def write_yaml(data: dict, file_name: str) -> None:
    # Create a file name matching the json file given as sys.argv[1]
    file_name = file_name.split(".")[0]

    with open(f"{file_name}.yaml", "w") as file:
        yaml.dump(data, file, sort_keys=False)
        print(f"successfully written to {file_name}.yaml")


files = ["example.json", "new_json_file.json", "new_file.json"]

for file_name in files:
    # storing return value from load_json as a variable called json_dict
    json_dict = load_json(file_name)

    # Passing json_dict variable (dictionary) to write_yaml
    write_yaml(json_dict, file_name)
