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

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())