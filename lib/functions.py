#!/usr/bin/env python3

def my_function(param):
    print("Running my_function")
    return param + 1

my_return_function_value = my_function(1)

print(my_return_function_value)

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    print(type(number))
    if type(number) == "int":
        return None
    
    return number / 2
