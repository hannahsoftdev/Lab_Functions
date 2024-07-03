# -*- coding: utf-8 -*-
"""Lab_Functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TOo_PUOXV49U12rpiwJwPyf4jwsfj_ya
"""

# 1. Functions for circumference and area of a circle

pi = 3.141592653589793 # value of pi

def circumference_calc(radius): # circumference function
  circumference = pi * (2 * radius) # circumference calculation
  return circumference # return value

def area_calc(radius): # area function
  area = pi * (radius * radius) # area calculation
  return area # return value

def radius_inp(): # main function
  radius = float(input("Enter the radius of the circle: ")) # user input

  circumference = circumference_calc(radius) # override
  area = area_calc(radius) # override

  print(f"A circle with a radius of {radius}")
  print(f"Has a circumference of {circumference:.2f}") # circumference with decimal format
  print(f"With an area of {area:.2f}")  # area with decimal format

radius_inp() # functino call

# 2. Function for area of a rectangle

# area of rectangle = length * width

def length_rec(): # length function
  length = float(input("Enter the length of the rectangle: ")) # user input
  return length # return value

def width_rec(): # width function
  width = float(input("Enter the width of the rectangle: ")) # user input
  return width # return value

def area_rec(): # area of rectangle function
  length = length_rec() # override
  width = width_rec() # override
  area = length * width  # area calculation

  print(f"A rectangle with a length of {length} and a width of {width}")
  print(f"Has an area of {area}")

area_calc() # function call

# Average of integers

def average_calc(num): # average number calculation function
  num_sum = 0 # sum of number given a value of zero
  for i in range (1, num+1): # for loop integer (from one, num_input + one)
    num_sum = num_sum + i # sum of number = sum of number + integer
  average = num_sum / num # average = sum of number / num_input
  return average # return value

def num_inp(): # main program function
  num = int(input("Enter an integer greater than 1: ")) # user input number greater than one

  average = average_calc(num) # override

  print(f"The average of the integers from 1 to {num} is {average}")

num_inp() # function call

# 4. Simple calculator

def add(x, y): # addition function
  return x + y # return value

def subtract(x, y): # subtraction function
  return x - y # return value

def multiply(x, y): # multiplication function
  return x * y # return value

def divide(x, y): # division function
  return x / y # return value

def calculator(): # main function
  print("Select operation.")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  choice = input("Enter choice (1/2/3/4): ") # user input

  n1 = float(input("Enter first number: ")) # user input
  n2 = float(input("Enter second number: ")) # user input

  if choice == '1': # if statement
    print(n1, "+", n2, "=", add(n1, n2)) # print statement
  elif choice == '2': # elif statement
    print(n1, "-", n2, "=", subtract(n1, n2)) # print statement
  elif choice == '3': # elif statement
    print(n1, "*", n2, "=", multiply(n1, n2)) # print statement
  elif choice == '4': # elif statement
    print(n1, "/", n2, "=", divide(n1, n2)) # print statement
  else: # else statement
    print("Invalid choice.") # print statement

calculator() # function call

