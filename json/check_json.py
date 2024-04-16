import sys
import os
import json

print(f"This is the name of the program: {sys.argv[0]}")
print(f"Number of elements including the name of the program: {len(sys.argv)}")
print(f"Number of elements excluding the name of the program: {(len(sys.argv)-1)}")
print(f"Argument List: {str(sys.argv)}")


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is valid.")
    else:
        print(f"no file found with name {sys.argv[1]}")
else:
    print("Please provide a json file name as 2nd argument.")
