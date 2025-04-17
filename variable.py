# variable = a container for a value. behaves as the value that it contains
# string = '' or "" is a var value

name = "misterback"
age = 19  #int = numbers
loves = "pizza"
print( "hello " + name,"your age is "+ str(age) , "you love " + loves)

print(type(name) , type(age))

#boolean = only stores whether its true or false
pizza = True
print(pizza)

rats = False
print(rats)

pizza = True
print("mister back loves pizza: " +str(pizza))

rats = False
print("mister back loves rats: " +str(rats))
print(type(pizza), type(rats))

#flot = are floating point integers
distance = 2.9
print(str(distance)+"kms")

print("hello "+name, "you like " +loves, "buts its "+str(distance) +"kms" ,"far")



awza = 5
print(id(awza))

import keyword
keyword.kwlist
print(keyword.kwlist)
print(len(keyword.kwlist))