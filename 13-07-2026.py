# create a python appn to design a function for a food delivery appn where the customer name is taken as positional argument and order type is default argument with default value regular the funcyion should accept the multiple food items ordered by the customer using positional argument and additional details such as address payment mode ,delivery instructions and discount using keyword argument the function should display the complete order summary including customer details list of items ordered total no of items and all additional information
def swiggy(customer_name,order_type="regular",*items,**details):
    print("Hi",customer_name)
    print("your order type is",order_type)
    print("List of items:")
    total_bill=0
    for item in items:
        print(item[0],":",item[1])
        total_bill+=item[1]
    if total_bill>200:
        total_bill=total_bill-total_bill*0.1
        print("after discount bill is",total_bill)
    else:
        print("total bill is",total_bill)
    print("number of items in cart:",len(items))
    print("additional details:")
    for key,value in details.items():
        print(key,":",value)
swiggy("abhi","zomato",["shawarma",100],["chicken roll",130],["coke",50],address="kphb",payment_mode="UPI",delivery_instruction="be in time")

def say_hi(name):
    print("hi",name)
greet=say_hi
greet("vamshi")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
calculate=[add,sub,mul]
print(calculate[1](30,20))
print([add,sub,mul][2](30,20))

# operations={
#     '+':add,
#     '-':sub,
#     '*':mul
# }
# op=input("Enter operation:")
# print(operations[op](20,30))





#Q1. Assign the built-in function len to a variable called count. Use it to find the length of a list.
list=[10,21,34,45,67]
count=len(list)
print(count)

# Q2. Write a function run_twice(func, value) that calls func on value twice and returns the final result.
def add(a):
    return a**2
def run_twice(func,value):
    return(func(func(value)))
print(run_twice(add,4))




# Q3. Store the functions upper, lower, and title (string methods) in a dictionary. Let the user choose which one to apply.
def upper(a):
    return a.upper()
def lower(b):
    return b.lower()
def title(c):
    return c.title()
str={
    'upper':upper,
    'lower':lower,
    'title':title
}
method=input("Enter any string(upper,lower,title):")
print(str[method]("kjibyub hgytbu fcrtft "))
    


# Q4. Write a function that returns another function. Example: make_multiplier(3) should return a function that multiplies any number by 3.

# Q5. Can you store the same function under multiple names in a dictionary? Test it and  explain what happens.
def see(name):
    print(name)

hello={
    'hi':see,
    'hi1':see
}
a=input("enter your name:")
hello['hi'](a)
hello['hi1'](a)
