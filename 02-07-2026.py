# Functions 
# def  calling a function
# parameters:giving information to the method

# we have types
# 1 without parameter without return value
# 2 without parameter with return value
# 3 with parameter without return value
# 4 with parameter with return  value

# 1 without parameter without return value
def m1():
    print("Hi class!")
m1()
print(m1())

# 2 without parameter with return value
def m1():
    print("Hi Class!")
    return 10
m1()
print(m1())

# 3 with parameter without return value
def m1(x):
    print(x)
m1(10)

def remainder(a,b):
    print(a%b)
remainder(10,2)

def learn(name,skill):
    print("Hi",name,"is learning",skill)
learn("Abhi","Python")

# 4 with parameter with return  value
def add(a,b):
    return a+b
add(10,30)
print(add(10,30))

def mod(a,b):
    return a%b
mod(20,4)
print(mod(20,4))

# Practice questions
# 1 write a function called say_hello() that prints 'Welcome to Python'
def say_hello():
    print("Welcome to python")
say_hello()

# 2 write a function called add(a,b) that returns the sum of two numbers
def add(a,b):
    print(a+b)
add(10,15)
# 3 what is the output of a function that has no return statement?write a function to verify this
def info(name,age):
    print("I am",name,"my age is",age)
info("abhi",22)
print(info("abhi",22))

# 4  Write a function area_of_rectangle(length, width) that returns length * width. Call it with values 6 and 4.
def area_of_rectangle(length,breadth):
    return length*breadth
print(area_of_rectangle(6,4))
# 5  Explain in your own words: why do we use functions instead of writing code directly?
# - to reuse  the code
#  -to reduce the code


