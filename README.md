# Scripting

When working with code (be it implementing new features, or interacting with existing functionality), we benefit from a
wealth of existing resources available. Resources like Stack Overflow are a great place to read up on how to implement
code, as well as best practices for a range of languages and libraries.

It makes sense to use the good work and knowledge available to us to improve our projects, and we don't have to limit
this to just writing code. Many programming languages benefit from an impressive library of pre-built classes and 
functions created to solve common problems, and python is no exception to this.

In fact, Python has perhaps one of the richest libraries of pre-built classes and functions. This functionality is 
typically bundled into either modules or packages. We can refer to using these modules as **Scripting**.

Instead of reinventing the wheel every time we need to do something, we are using existing code.

## Benefits of scripting
- Makes our code more human-readable by abstracting away much of the logic.
- Our applications behaviour is more predictable when using pre-built functions. Documentation, as well as behaviour is widely understood and available.
- Other programmers will be familiar with popular modules and their use, so it will be easier for other people to use our app.
- Popular modules will already be used in other parts of larger applications. We aren't repeating outselves.

![Scripting vs Programming](https://visionx.io/wp-content/uploads/2023/03/Scripting-Language-vs-Programming-Language-300x300.png)

##Popular python libraries 
Python comes with many useful built-in libraries (collections of useful classes and functions). Here are some examples:

````python
import datetime
import json

def unnecessary_function(date_string: str) -> datetime.date:
    return datetime.date.fromisoformat(date_string)

print(unnecessary_function("2024-04-15"))


def load_json(file_name: str) -> dict:
    """Opens and loads a json file then returns."""
    try:
        file = open(file_name, "r", encoding="UTF-8")
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Error! {file_name} is an invalid path.") from exc
    else:
        with file:
            data = json.load(file)
            return data

````
As well as being widely used, tested and understood, many of these built-in libraries make use of lower-level 
programming. This makes them more efficient, a very useful trait when working with larger applications and datasets.

We can write scripts to make the most of this existing functionality.

## Examples of scripts a DevOps engineer might use

1) Reading and writing information to and from a database
2) Concurrent programming and waiting for responses from a server (async)
3) Working accurately with large numbers or datasets
4) Formatting print statements in an error message (color, bold or layout)
5) Testing with a suite like pytest
6) Providing access to the hardware layer
7) Bringing in and converting data (json)
8) Exiting the application when appropriate (sys.exit)
9) Abstracting, or hiding, paths and environment variables
10) Detecting the OS the python app is running on
