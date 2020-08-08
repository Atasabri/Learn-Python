import requests
import subprocess
from string import Template
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import webbrowser
import string
import random
from datetime import datetime, timedelta
import time
import sqlite3
import json
import csv
from zipfile import ZipFile
from time import ctime
import shutil
from pathlib import Path
from TestPackage.TestModule import testpackage
from TestPackage.TestSubPackage.TestSubPackageModule import testsubpackage
from Preview import func
from abc import ABC, abstractmethod
from array import array
import math
print("Hello World !")

# Variables
"""
Id = 1
print(Id)
first_name = "Ata"
print(first_name)
is_found = True
print(is_found)
"""
# Strings
full_text = """
hi,
My Name Is Ata Sabri Ata
From Egypt .
"""
"""
name = "Ata Sabri Ata Ahmed"


print(name)
print(full_text)
print(len(name))
print(name[2])
print(name[1:4])
print(name[-1])
"""

# Escape Sequences

"""
name1 = "Ata \n sabri"
name2 = "Ata \" sabri"

print(name1)
print(name2)
"""

# Formated String
# Concatination
"""
first_name = "Ata"
last_name = "Sabri"
full = first_name + " " + last_name
print(full)
good_full = f"{first_name} {last_name}"
print(good_full)
"""

# String Methods
"""
name = "ata sabri"
print(name.upper())
print(name.title())
print(name.__add__(" ahmed"))
print(name.__contains__("ata"))
print("ata" not in name)
print("ata" in name)
print(name.find("s"))
print(name.find("k"))
print(name.replace("a", "N"))
print(name.strip())   # Remove L & R Spaces
print(name.isalnum())
print(name.isalpha())
print(name.istitle())
"""

# Numbers
"""
print(10 ** 3)  # Power
print(10 % 3)

print(math.ceil(2.2))
print(math.pow(10, 2))
"""
# Convertion
"""
x = input("X: ")
y = int(x) + 1
print(y)

print(bool(0))
print(bool(None))
print(bool(""))
print(bool(1))
print(bool(-1))
print(bool("Test"))
print(bool("False"))
"""

# If Statment
"""
name = "ata"
if name == "ata":
    print("Your Name Is : Ata Sabri Ata")
    print("Thanks Ata.")
elif name == "sabri":
    print("Your Name Is : Sabri Ata Ahmed")
    print("Thanks Sabri.")
else:
    print("Thank You.")
print("All Is Done .")
"""

# Ternary Operator
"""
age = 20
message = "You Are +18" if age >= 18 else "You Can Access You -18"
print(message)
"""

# Operators
"""
found = True
active = False
selected = True

if not found:
    print("condition 1")
if found or active:
    print("condition 2")
if found and active:
    print("condition 3")
if (found or active) and selected:
    print("condition 4")

"""

# Chaining
"""
age = 22
if 18 < age < 60:
    print("Accepted Date")
"""

# Loops
"""
for number in range(4):
    print(number)

for number in range(1, 4):
    print(number)

for number in range(1, 6, 2):  # Range (initial Value , Value ,Increment Value)
    print(number)

for number in range(10):
    print(number)
    if number == 5:
        print("55555555")
        continue
else:
    print("Loop Finish Done .")
for number in range(10):
    print(number)
    if number == 5:
        print("55555555")
        break
else:
    print("Loop Finish Done .")

"""

# Nested Loops
"""
for i in range(5):
    for j in range(3):
        print(f"({i} , {j})")

"""

# While Loops
"""
command = ""

while command.lower() != "quit":
    command = input()
    print(f"You Enter : {command} ")
else:
    print("You Quit App .")

"""

# Functions

"""
def printName(name):
    print(f"My Name Is : {name}")


def get_full_name(firstname, lastname):
    return f"{firstname} {lastname}"


def testdefaultparam(name, age=24):
    printName(f"Your name Is : {name} And Age Is : {age}")


def testMultiParams(*names):  # Xargs Function
    for name in names:
        print(name)


def testXXargs(**user):  # XXargs Function
    print(user)
    print(user["id"])
    print(user["Name"])
    print(user["Age"])


printName("Ata Sabri Ata Ahmed")
print(printName("AtaSabri"))  # Default REturn Of Functions Is None
print(get_full_name("Ata", "Sabri"))

testdefaultparam("Ata Sabri")
testdefaultparam("Ata Sabri", 33)

testMultiParams(2, 3, 4)  # Call Xargs Function
testXXargs(id=1, Name="Ata Sabri", Age=24)


"""

# Lists
"""
letters = ["A", "B", "C", "D", "E"]
print(letters)
for letter in letters:
    print(letter)


numbers = list(range(1, 20))
print(numbers)
print(*numbers)

matrix = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
for i in matrix:
    for j in i:
        print(j)

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

first, second, *other = numbers  # Assign List Items To Variables
print(first, second, other)

for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)

print(" ".join(letters))
"""
# List Methods
"""
letters = ["A", "B", "C", "D", "E"]

letters.append("F")  # Append Item
print(letters)
letters.insert(3, "E")  # Insert Item
print(letters)
letters.remove("E")  # Remove Item
print(letters)
letters.pop()  # Delete Last Item
print(letters)
letters.pop(1)  # Delete Index Of 1
print(letters)
# del letters[2]  # Delete index Of 2
print(letters)
print(letters.count("A"))
print(letters.index("A"))
print("D" in letters)
print(letters.__contains__("D"))

"""

# List Sorting

"""

numbers = [1, 2, 3, 4, 5, 6, 7]
print(sorted(numbers, reverse=True))
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

"""

# List Tuple Sorting

"""
Items = [
    ("ata", 12),
    ("sabri", 33),
    ("ahmed", 11)
]

print(Items)
print(Items[0])
print(Items[0][0])


def sort_items(item):
    return item[1]


Items.sort(key=sort_items)
print(Items)

"""

# List Select Methods
"""
data = [
    ("Ata", 24),
    ("Sabri", 33),
    ("Ahmed", 55),
    ("Heba", 22),
]

print(list(map(lambda item: item[1], data)))

print([item[0] for item in data])

print(list(filter(lambda item: item[1] >= 24, data)))

print([item for item in data if item[1] >= 24])

"""

# Zip Function
"""
numbers = [1, 2, 3, 4]
letters = ["a", "b", "c", "d"]

print(list(zip(numbers, letters)))
print(list(zip("atas", numbers, letters)))

"""

# Swapping
"""
x = 10
y = 11

x, y = y, x

print(x, y)

"""

# Arrays
"""
numbers = array("i", [1, 2, 3])
names = array("u", ["a", "s", "d"])

print(list(numbers))
print(list(names))

"""

# Sets
"""
numbers = [1, 2, 3, 4, 5]
set1 = set(numbers)
set2 = {2, 4, 5, 6, 7, 8}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

"""

# Dictionaries
"""
data = {"x": 1, "y": 2, "z": 3}

data = dict(x=1, y=2, z=3)

for item in data:
    print(item)
for key, value in data.items():
    print(key, value)

for value in data.values():
    print(value)

print(data)

"""
# Handle Exceptions
"""
try:
    age = int(input("Enter Your Age : "))
    print(100/age)
except Exception as ex:
    print(ex)
else:
    print("Done .")
finally:
    print("Finally Code .")


try:
    age = int(input("Enter Your Age : "))
    print(100/age)
except (ValueError, ZeroDivisionError) as ex:
    print(ex)
else:
    print("Done .")
finally:
    print("Finally Code .")

"""

# Raise Exceptions  (Bad Preformance)

"""
def test(age):
    if(age == 0):
        raise ZeroDivisionError("Can Not Divide By Zero .")
    print(100/age)


try:
    test(int(input("Enter Your Age : ")))
except Exception as ex:
    print(ex)

"""

# Classes

"""
class Ata:

    color = "red"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def draw(self):
        print("From Draw Functipon In Ata Class .")

    def print_data(self):
        print(f"Your Name Is : {self.name} & Your Age Is : {self.age}")


Ata.color = "white"  # Accross All Instances


ata = Ata("Ata Sabri Ahmed", 24)
print(ata.color)
ata.color = "yellow"
print(ata.color)  # Just For ata Instance
ata.draw()
print(isinstance(ata, Ata))
ata.print_data()

ata2 = Ata("Ata Sabri", 12)
print(ata2.color)
"""


# Class & Static Methods
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(1, 2)

    @staticmethod
    def get_data():
        print("Get All Data")


point = Point.zero()
point.get_data()

"""
# Magic Methods

"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):   # __str__ Is A Magic Method Like Override
        return f"Point : ({self.x} , {self.y})"


point = Point(1, 2)
print(point)

"""
# Comparing Magic Methods
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other = Point(1, 2)

print(point == other)
print(point > other)

"""

# Operations Magical Method

"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __str__(self):
        return f"Point Is : ({self.x} , {self.y})"


point = Point(1, 2)
other = Point(2, 3)

final = point + other
print(final)

"""
# Container
"""

class Point:
    def __init__(self):
        self.tags = {}

    def __setitem__(self, tag, value):
        self.tags[tag] = value

    def __len__(self):
        return len(self.tags)

    def __getitem__(self, tag):
        return self.tags[tag]

    def __iter__(self):
        return iter(self.tags)

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0)+1


point = Point()

point.add("python")
point.add("python")
point.add("python")

for item in point:
    print(item, point[item])

print(len(point))
point["python"] = 10

for item in point:
    print(item, point[item])

"""

# Private Members
"""

class Point:
    def __init__(self):
        self.__privatemember = 10  # Adding __ at First Of Member To Make It Private


point = Point()

print(point.__privatemember)  # Print Not Found


"""

# Properites Using Decoder
"""

class Point:
    def __init__(self, name):
        self.__name = name

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if("Ata" in value):
            self.__name = value
        else:
            self.__name += " Ata"


point = Point("Ata Sabri")
print(point.Name)
point.Name = "Ahmed"
print(point.Name)

"""


# Properites Using Property Function
"""
class Point:
    def __init__(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def __set_name(self, value):
        if("Ata" in value):
            self.__name = value
        else:
            self.__name += " Ata"

    Name = property(__get_name, __set_name)


point = Point("Ata Sabri")
print(point.Name)
point.Name = "Ahmed"
print(point.Name)

"""

# Inheritance
"""

class Animal:
    def __init__(self):
        self.name = "Ata"

    def eat(self):
        print("Eating")


class Cat(Animal):
    def walk(self):
        print("walk")


cat = Cat()
cat.eat()
cat.walk()

print(isinstance(cat, Cat))
print(isinstance(cat, Animal))
print(isinstance(cat, object))
print(issubclass(Cat, Animal))
print(issubclass(Cat, object))

"""

# Overriding

"""
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} with age : {self.age} is Eating")

    def testoverride(self):
        print("Method From Animal Class .")


class Cat(Animal):
    def __init__(self, age, weight):
        super().__init__("Cat", age)
        self.weight = weight

    def testoverride(self):
        # super().testoverride()
        print("Method From Cat Class .")

    def walk(self):
        print(f"{self.name} with age : {self.age} is Walking")


cat = Cat(12, 10)
cat.eat()
cat.walk()
cat.testoverride()

"""

# Multi Inheritance
"""

class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("Eat From Animal Class .")


class Bird:
    def __init__(self):
        pass

    def eat(self):
        print("Eat From Bird Class .")


class Checken(Bird, Animal):
    def __init__(self):
        pass


checken = Checken()
checken.eat()  # Excute Method In First Parent Class

"""
# Abstract Class & Abstract Method

"""
class Animal(ABC):   # ABC Mean Abstract Base Class
    def test(self):
        print("Testing")

    @abstractmethod  # For Make Method Absract Method
    def eat(self):
        pass


class Cat(Animal):
    def eat(self):
        print("Cat Eating")


cat = Cat()
cat.eat()

"""

# Ploymorphism

"""
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Draw TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("Draw DropDownList")


def drawControl(control):
    control.draw()


textbox = TextBox()
ddl = DropDownList()

drawControl(textbox)
drawControl(ddl)

"""

# Modules

"""
from Preview import func
from Preview import *

func()

"""

# Packages  (Folder has file (__init__.py))
"""

# from TestPackage.TestModule import testpackage

testpackage()

"""
# SubPackage (Sub Folder has File (__inti__.py))

"""
# from TestPackage.TestSubPackage.TestSubPackageModule import testsubpackage

testsubpackage()

"""

# Main Data
"""
print(__name__)
print(__file__)
print(__package__)
print(__doc__)

"""

# Path
"""

path = Path("TestPackage/TestModule.py")
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

print(path.is_absolute())
print(path.is_file())
print(path.is_dir())

print(path.with_name("ata.txt"))
print(path.with_suffix(".txt"))

"""

# Directories
"""
path = Path("TestPackage")

print(path.is_dir())
print(path.exists)

# path.rename("TestPackage") # Rename Dir Name
# path.mkdir()  # Create Dir If Not Exists
# path.rmdir()  # Remove Dir If Empty

data1 = [p for p in path.iterdir()]
data2 = [p.name for p in path.glob("*.py")]
print(data1)
print(data2)

"""

# Files
"""
path = Path("TestPackage/TestModule.py")

print(path.exists())
print(path.name)
print(path.read_text())

# from time import ctime
print(ctime(path.stat().st_ctime))

# path.rename("new Name")  # Rename
# path.unlink()       # Delete File

path.write_text(path.read_text() + "\n # Write Using Python Code .")
print(path.read_text())

# import shutil

path1 = Path() / "ata.py"

shutil.copy(path, path1)

"""


# open() Method

"""
file = open("TestPackage/ata.py", "x")  # Create New File
file.write("# Test Code Using open() Method .")  # Write To File
file.close()  # Close File

"""

"""
print(open("TestPackage/ata.py", "r").read())  # Read From File

# Read From File Line By Line
print(open("TestPackage/ata.py", "r").readlines())

"""

# With Statment (Like Using in C # )

"""
with open("TestPackage/TestModule.py", "r") as file:
    print(file.read())

"""

# Zip Files

# from zipfile import ZipFile
"""
with ZipFile("files.zip", "a") as file:
    for f in Path("TestPackage").iterdir():
        file.write(f)

"""
"""
with ZipFile("files.zip") as file:
    print(file.namelist())
    # Get File Info
    info = file.getinfo("TestModule.py")
    print(info.compress_size)
    print(info.file_size)

    # Extract All Files & Folders To Folder (ExtractFolder)
    file.extractall("ExtractFolder")

"""


# Excel Files
"""
# import csv


with open("ata.csv", "r") as file:
    # Write To CSV File

    writer = csv.writer(file)
    writer.writerow(
        ["Name", "Age", "Number"]
    )
    writer.writerows(
        [["Ata Sabri", "24", "01142229025"], ["Ata Ahmed", "33", "01142229025"]]
    )

    # Read From CSV
    reader = csv.reader(file)
    for row in reader:
        print(row)
"""

# Json
"""
# import json

movies = [{"Id": 1, "Name": "Ata Sabri"}, {"Id": 2, "Name": "Ahmed Ata"}]
data = json.dumps(movies)
print(data)
Path("atasabri.json").write_text(data)

reloadeddata = Path("atasabri.json").read_text()

print(json.loads(reloadeddata))

"""

# Sqlite

"""
# import sqlite3

data = json.loads(Path("atasabri.json").read_text())

with sqlite3.connect("db.DB") as connect:

    command = "INSERT INTO FirstTable VALUES (?, ?)"
    for item in data:
        print(tuple(item.values()))
        connect.execute(command, tuple(item.values()))
    connect.commit()

    select_command = "Select * from FirstTable"
    curser = connect.execute(select_command)
    print(curser.fetchall())

"""

# Time

"""
# import time

def fun():
    for ii in range(10000):
        pass


start = time.time()

fun()

end = time.time()

print(end - start)

"""

# DateTime
"""
#from datetime import datetime,timedelta

print(datetime.now())

print(datetime.timestamp(datetime.now()))

print(datetime.now().date())

print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)

print(datetime.now().strftime("%A"))
print(datetime.now().strftime("%a"))
print(datetime.now().strftime("%B"))

dt = datetime(2020, 1, 2)
print(dt.strftime("%y"))

dt1 = datetime(2018, 1, 1)
dt2 = datetime(2020, 1, 1)

duration = dt-dt1
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.total_seconds())

# timeDelta
dtDelta = dt1+timedelta(days=1, seconds=10)
print(dtDelta)

"""
# Random

"""
#import random
#import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 10, 9]))
print(random.choices([1, 2, 3, 5, 6, 3], k=3))
print(random.choices("abcdefghijkl1239ufjdfj", k=4))
print(random.choices(string.ascii_letters, k=4))
print(random.choices(string.digits, k=4))
print(random.choices(string.ascii_letters + string.digits, k=4))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

numbers = [1, 5, 3, 6, 8]
random.shuffle(numbers)
print(numbers)

"""

# Web Browser
"""
#import webbrowser

print("opening browser ....")
webbrowser.open("www.google.com")

"""

# Emails
"""
#from email.mime.multipart import MIMEMultipart
#from email.mime.image import MIMEImage
#from email.mime.text import MIMEText
#import smtplib

message = MIMEMultipart()
message["from"] = "Ata Sabri"
message["to"] = "ataeldon@gmail.com"
message["subject"] = "Test"

message.attach(MIMEText("This Is From Python Test ."))
message.attach(MIMEImage(Path("Ata.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("asabri@itpseg.com", "AS@123123")
    smtp.send_message(message)

print("Sent Done .")

"""

# Email Templates

"""
#from string import Template

message = MIMEMultipart()
message["from"] = "Ata Sabri"
message["to"] = "ataeldon@gmail.com"
message["subject"] = "Test"

template = Template(Path("template.html").read_text())
body = template.substitute({"name": "Ata Ahmed"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("Ata.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("asabri@itpseg.com", "AS@123123")
    smtp.send_message(message)

print("Sent Done .")

"""

# Running Extrnal Program
"""
#import subprocess

completed = subprocess.run(["echo", "Hiiiiiiii"], shell=True)

print(completed.args)
print(completed.returncode)
print(completed.stderr)
print(completed.stdout)

"""

# Requests

"""
# Pip (PyPi) pypi.org

# in cmd ==> pip install requests

#import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())

"""
