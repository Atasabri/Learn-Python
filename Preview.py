
# Variables
# Strings
# Escape Sequences
# Concatination
# Numbers
# Convertion
# If Statment
# Ternary Operator
# Operators
# Chaining
# For Loops
# While Loops
# Functions


# Lists   =========== >> [1,2,3,4]  list()
# Sets    =========== >> {1,2,3,4}  set()
# Tuples  =========== >> (1,2,3,4)  tuple()
# Dictionaries ====== >> {"key":value,"key":value} dict()
# Arrays  =========== >> array("i",[1,2,3,4])       array()
# Itrable (Range) === >> range(5)


# Classes
# Private Members
# Properites (Decoder , Function)
# Constractor
# Container
# Multi Inheritance
# ClassMethod & Static Method
# Overriding (super()) , Magic Methods
# Abstract Class & Abstract Method
# Polymorphism


# Module
# Package
# Sub Package


# Working With Path
# Working With Directories
# Working With Files
# Working With Zip Files
# Working With Excel Files
# Working With Json Files (Json Data)
# Working With Sqlite
# Time
# DateTime , TimeDelta
# Random
# string Module
# webbrowser
# Emails (Tempaltes)
# SubProcess

# Pip
# Virtual Environment
# Pipenv
# Publish Package

"""
testlist = [1, 2, 3, 4, 5]
testset = {1, 2, 3, 4, 5}

final = [*testset, *testlist, *"Hello"]

print(final)


cvcv = [x+1 for x in testlist]
print(type(cvcv))
print(cvcv)
cvcv = [x for x in testlist if x > 3]
print(type(cvcv))
print(cvcv)
cvcv = {x for x in testlist}
print(type(cvcv))
print(cvcv)
cvcv = {f"key :{x}": x for x in testlist}
print(type(cvcv))
print(cvcv)

"""
"""
listtest = {"key1": 1, 1: "ata", "key2": 23, 2: "sabri"}
for item in listtest.items():
    print(item)
"""
"""
listtest1 = [1, 2]
listtest2 = [2, 3]

final = listtest1 + listtest2
print(final)
"""
"""
from array import array
names = array("i", [1, 2])

"""

"""
def namelist(names):
    names = [x["name"] for x in names]
    return "" if not names else names[0] if len(names) == 1 else ", ".join(names[:-1])+" & "+names[-1]


print(namelist([]))
"""

"""
class Point:
    def __init__(self):
        self.__name = "Ata"

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name == value


point = Point()
print(point.Name)

"""




from functools import wraps
import time
import numpy as np
import openpyxl
from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
import enum
def func():
    print("Test Modules")


# Delegates
"""
def test(func):
    items = ["ata", "sabri", "ahmed"]

    return [item for item in items if func(item)]


print(test(lambda item: len(item) == 3))

"""

# Enums
"""
class Days(enum.Enum):
    Sat = 1
    Sun = 2
    Mon = 3


print(Days.Sat)
print(Days.Sat.value)
print(Days["Sat"])
print(Days(1))

"""
# Yelp API

"""
api_key = "nID9kjzhdrX9do4ZBWcJUCMhTvndOQ8Da1zZQTHJYlSpO095EOxZQTHWRm4eeEwgBzBQZtO32qZVeZtpgANInqrpoBVTiSYU2NKUbPck6u8bZy1uKWhF4pcBntP_XnYx"
headers = {
    "Authorization": "Bearer "+api_key
}

params = {
    "term": "rest",
    "location": "NYC"
}

response = requests.get(
    "https://api.yelp.com/v3/businesses/search", headers=headers, params=params)

print(response.json())

"""

# Twilio

"""
client = Client("ACfabd06920871533bfe7a82b07b501e9c",
                "a49e11aee97dcb81871cf8ae96afac95")

client.messages.create(
    to="+201142229025",
    from_="+12058437373",
    body="Test"
)

"""

# Web Scraping (Get StackOverFolw Questions)
"""

response = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(response.text, "html.parser")

applications = soup.select(".question-summary")
# print(applications)

for item in applications:
    print(item.select_one(".question-hyperlink").getText())

"""

# NumPy  (Work With Arrays & Matrixs Very very well)

"""
array = np.array([1, 2, 3, 4])  # 1 Dimention
print(array)
array = np.array([[1, 2], [3, 4]])  # 2 Dimention
print(array)
print(array[0, 1])
print(array > 1)


array = np.zeros((2, 2))
print(array)
array = np.zeros((2, 2), int)
print(array)
array = np.ones((2, 2))
print(array)
array = np.full((2, 2), 5)
print(array)
array = np.random.random((2, 2))
print(array)
print(np.round(array))
array = np.random.randint(1, 10, (2, 2), int)
print(array)


first = np.array([[1, 2], [2, 3]])
second = np.array([[1, 2], [2, 3]])

print(first + second)
print(first * 2)
print(first + 3)


"""

# Wrapper Function
"""
def checktime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print(end - start)

        return func(*args, *kwargs)

    return wrapper


nnnn = 0


@checktime
def printloop():
    global nnnn
    count = 0
    nnnn += 1
    for i in range(1, 10):
        count += i

    return count


printloop()
print(nnnn)
"""
