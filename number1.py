"""
Program to check whether a given number is an even number or not
"""
from ast import Num
from tkinter import N


while True:
       print("To cancel, Enter 00")
       number = eval(input("Enter any number: "))
       if number == 00:
              print("Program terminated")
              break
       elif number % 2 == 0:
              print(f"{number} is an even number")
       else:
              print(f"{number} is not an even number")