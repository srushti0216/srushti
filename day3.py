# def my_function():
#   print("Hello from a function")

# my_function()

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")

# def calc():
#   a=10
#   b=20
#   if a<b:
#     print('a is less than b')
#   else:
#     print('a is greater than b')

# calc()

# def myfunc():
#   x = 300
#   print(x)

# myfunc()

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())

# x = lambda a : a + 10
# print(x(5))

# def countdown(n):
#   if n <= 0:
#     print("Done!")
#   else:
#     print(n)
#     countdown(n - 1)

# countdown(5)

# def count_up_to(n):
#   count = 1
#   while count <= n:
#     yield count
#     count += 1

# for num in count_up_to(5):
#   print(num)

# def count_up_to(n):
#   count = 1
#   while count <= n:
#     yield count
#     count += 2

# for num in count_up_to(10):
#   print(num)

# height = float(input('enter your height in cm:'))
# weight = float(input('enter your weight in kg:'))

# # Convert cm to meters
# height = height / 100

# bmi = weight / (height * height)
# print('your bmi is:', round(bmi, 2))

# if bmi < 18.5:
#     print('underweight')
# elif bmi < 25:
#     print('normal')
# elif bmi < 30:
#     print('overweight')
# else:
#     print('obese')

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Linus", 28)
# p2 = Person('Srushti',24)

# print(p1.name)
# print(p1.age)

# print('Name:',p2.name,' ','Age:',p2.age)

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()