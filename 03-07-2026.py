# Function
#Function is a block of code that is used to perform a set of actions
# Functions are easier because they provide reusability of code
# they are easier to correct,debug and improve readability
# Syntax: def functionname(parameters):
            # body of function/lines of code
            # return type  # optinal
 
def greet(name):
    print("Hi!",name)
greet("Abhi")

def say_hello():
    print("Welcome to python!")
say_hello()
def add(a,b):
    print("this is add method")
    print(a+b)
add(10,20)
say_hello()

def add(a,b):
    print(a+b)
add(10,20)

def sub(a,b):
    print(a-b)
sub(30,10)

def mul(a,b):
    print(a*b)
mul(7,4)

def div(a,b):
    print(a/b)
div(24,6)

def area_of_rectangle(length,width):
    x=length*width
    return x
area_of_rectangle(20,30)
print(area_of_rectangle(20,30))

def area_of_rectangle(length,width):
    x=length*width
    return x
area_of_rectangle(20,30)
area=area_of_rectangle(20,30)
print(area)

def add(a,b):
    return a+b
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return a/b
x=add(10,20)
y=sub(20,30)
z=mul(x,y)
print(div(z,10))