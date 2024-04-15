"""File to demonstrate how we can use the python standard library."""
import datetime
# Python standard library

# The standard library consists of many modules and packages that are very useful.
# These come with python by default.

# Random demo
import random
import math
import os
import sys
import builtins
import requests

print(random.random())
print(random.randrange(1,10))

# Math demo
print(f"\n{'='*20}math demo{'='*20}")
num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
print(f"Remainder from 1/5 {math.remainder(1,5)}")

# os demo
print(f"\n{'='*20}os demo{'='*20}")
working_dir = os.getcwd()
print(f"Current working directory {working_dir}")

username = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"username is {username}")

cpu_cores = os.cpu_count()
print(f"Number of CPU cores is {cpu_cores}")


# sys module
print(f"Current path: {sys.path}")
print(sys.version)

example_date = datetime.time
print(example_date)

# requests demo

request_bbc = requests.get("https://www.bbc.co.uk")
print(request_bbc.status_code)
