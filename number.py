#This defines a module that will be imported in another module
import string
from turtle import stamp


class DefinedClass:
       def prettyPrint(string):
              return print(f"*****{string}*****")
dc = DefinedClass
# print(dc.prettyPrint())