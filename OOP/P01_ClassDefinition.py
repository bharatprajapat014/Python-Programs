#Author: OMKAR PATHAK
#In this program we will see how to define a class

class MyFirstClass():
    #Class Attributes
    var = 10

firstObject = MyFirstClass()      #Object name = firstObject
print(firstObject)      #Printing object's memory hex
print(firstObject.var)  #Accessing Class Attributes

secondObject = MyFirstClass()
print(secondObject)
print(secondObject.var)
