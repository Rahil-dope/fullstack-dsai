print("Hello, World!")
# Python Basic Syntax Examples
# This program demonstrates all basic Python syntax with examples

# 1. Variables and Data Types
print("=== 1. Variables and Data Types ===")

# Integer
age = 25
print(f"Integer: age = {age}, type: {type(age)}")

# Float
height = 5.9
print(f"Float: height = {height}, type: {type(height)}")

# String
name = "Alice"
print(f"String: name = '{name}', type: {type(name)}")

# Boolean
is_student = True
print(f"Boolean: is_student = {is_student}, type: {type(is_student)}")

# List
fruits = ["apple", "banana", "cherry"]
print(f"List: fruits = {fruits}, type: {type(fruits)}")

# Tuple
coordinates = (10, 20)
print(f"Tuple: coordinates = {coordinates}, type: {type(coordinates)}")

# Dictionary
person = {"name": "Bob", "age": 30, "city": "New York"}
print(f"Dictionary: person = {person}, type: {type(person)}")

# Set
unique_numbers = {1, 2, 3, 2, 1}
print(f"Set: unique_numbers = {unique_numbers}, type: {type(unique_numbers)}")

# 2. Operators
print("\n=== 2. Operators ===")

# Arithmetic operators
a = 10
b = 3
print(f"Arithmetic: a + b = {a + b}, a - b = {a - b}, a * b = {a * b}, a / b = {a / b}, a // b = {a // b}, a % b = {a % b}, a ** b = {a ** b}")

# Comparison operators
print(f"Comparison: a == b: {a == b}, a != b: {a != b}, a > b: {a > b}, a < b: {a < b}, a >= b: {a >= b}, a <= b: {a <= b}")

# Logical operators
x = True
y = False
print(f"Logical: x and y: {x and y}, x or y: {x or y}, not x: {not x}")

# Assignment operators
c = 5
c += 2  # c = c + 2
print(f"Assignment: c += 2, c = {c}")

# 3. Control Structures
print("\n=== 3. Control Structures ===")

# If-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"If-elif-else: score {score} = grade {grade}")

# For loop
print("For loop:")
for i in range(5):
    print(f"  Iteration {i}")

# For loop with list
print("For loop with list:")
for fruit in fruits:
    print(f"  {fruit}")

# While loop
print("While loop:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1

# 4. Functions
print("\n=== 4. Functions ===")

def greet(name):
    """Function with parameter and return value"""
    return f"Hello, {name}!"

def add_numbers(x, y):
    """Function with multiple parameters"""
    return x + y

def print_info(*args, **kwargs):
    """Function with variable arguments"""
    print("Args:", args)
    print("Kwargs:", kwargs)

print(greet("World"))
print(f"5 + 3 = {add_numbers(5, 3)}")
print_info("apple", "banana", name="Alice", age=25)

# 5. Classes and Objects
print("\n=== 5. Classes and Objects ===")

class Person:
    """Simple class example"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

    @staticmethod
    def species():
        return "Human"

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous", 0)

# Create objects
person1 = Person("Charlie", 28)
person2 = Person.create_anonymous()

print(person1.introduce())
print(person2.introduce())
print(f"Species: {Person.species()}")

# 6. Exception Handling
print("\n=== 6. Exception Handling ===")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception caught: {e}")
finally:
    print("This always executes")

# 7. File Operations
print("\n=== 7. File Operations ===")

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# 8. List Comprehensions
print("\n=== 8. List Comprehensions ===")

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Original: {numbers}")
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# 9. Dictionary Comprehensions
print("\n=== 9. Dictionary Comprehensions ===")

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_comp = {k: v for k, v in zip(keys, values)}
print(f"Dictionary comprehension: {dict_comp}")

# 10. Lambda Functions
print("\n=== 10. Lambda Functions ===")

square = lambda x: x**2
add = lambda x, y: x + y
print(f"Lambda square of 5: {square(5)}")
print(f"Lambda add 3 + 4: {add(3, 4)}")

# Sorting with lambda
data = [('Alice', 25), ('Bob', 30), ('Charlie', 20)]
sorted_data = sorted(data, key=lambda x: x[1])
print(f"Sorted by age: {sorted_data}")

# 11. Modules and Imports
print("\n=== 11. Modules and Imports ===")

import math
import datetime

print(f"Math sqrt(16): {math.sqrt(16)}")
print(f"Current date: {datetime.date.today()}")

# 12. Input and Output
print("\n=== 12. Input and Output ===")

# Input (commented out to avoid blocking)
# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")

# Formatted output
name = "David"
age = 35
print(f"Formatted: My name is {name} and I am {age} years old.")
print("Old style: My name is %s and I am %d years old." % (name, age))

# 13. String Operations
print("\n=== 13. String Operations ===")

text = "Hello, Python World!"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Split: {text.split()}")
print(f"Replace: {text.replace('Python', 'Amazing Python')}")
print(f"Substring: {text[7:13]}")

# 14. List Operations
print("\n=== 14. List Operations ===")

my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")
my_list.append(6)
print(f"After append: {my_list}")
my_list.insert(0, 0)
print(f"After insert: {my_list}")
my_list.remove(3)
print(f"After remove: {my_list}")
print(f"Index of 4: {my_list.index(4)}")
my_list.sort(reverse=True)
print(f"After sort reverse: {my_list}")

# 15. Dictionary Operations
print("\n=== 15. Dictionary Operations ===")

my_dict = {"name": "Eve", "age": 22, "city": "London"}
print(f"Original dict: {my_dict}")
my_dict["country"] = "UK"
print(f"After adding country: {my_dict}")
print(f"Keys: {list(my_dict.keys())}")
print(f"Values: {list(my_dict.values())}")
print(f"Items: {list(my_dict.items())}")
del my_dict["age"]
print(f"After deleting age: {my_dict}")

print("\n=== Program completed! ===")
