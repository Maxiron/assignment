#This defines a module that will be imported in another module

class DefinedClass:
       def prettyPrint(string):
              return print(f"*****{string}*****")
dc = DefinedClass
# print(dc.prettyPrint())
