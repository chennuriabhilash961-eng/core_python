def trip_details(driver_name,pickup_location,drop_location,fare):
    print("your driver name is",driver_name)
    print("from",pickup_location)
    print("to",drop_location)
    print("fare is",fare)
trip_details("Abhilash","Hyderabad","Bangalore",500)
trip_details(fare=432,drop_location="jntu",pickup_location="Hyderabad",driver_name="Ajay")

trip_details("subbu","kphb",drop_location="jntu",fare=400)

# default 
def greet(name="user"):
    print("Hello!",name)
greet("arun")
greet()

def hello(age,name="user"):
    print("Hello!",name)
    if age>18:
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote")
hello(20)
hello(15,"arun")

# Q1. Write a function power(base, exponent=2) that returns base^exponent. Test with one
# and two arguments.
def power(base,exponent=2):
    return base**exponent
print(power(8))
print(power(3,4))
print(power(base=4)) # without default value
print(power(exponent=3,base=4))# with default
# Q2. Create a function connect(host, port=3306, protocol='TCP') and call it with various
# combinations.
def connect(host,port=3306,protocol="Tcp"):
    print("your host is",host)
    print("port is",port)
    print("protocol is",protocol)
connect("server")
connect("cloud",port=404,protocol="Http")
connect("localhost",443,"udp")
connect(host="client",port=442,protocol="https")
# Q3. What is the SyntaxError in: def func(name='Guest', age)? Fix it.
# def func(name="guest",age):
#     print("Hi!",name)
#     if age>18:
#         print("eligible for vote")
#     else:
#         print("not eligible for vote")
# func("abhi",14)
# SyntaxError: parameter without a default follows parameterwith a default
def func(age,name="guest"):
    print("Hi!",name)
    if age>18:
        print("eligible for vote")
    else:
        print("not eligible for vote")
func(21)
func(15,"abhi")
func(age=27,name="arun")
func(age=45)

# Q4. Write a function discount_price(price, discount=10) that returns the discounted price.
# Test with and without the discount argument.
def discount_price(price,discount=10):
    discount=price-discount
    return discount
print(discount_price(150))
print(discount_price(150,20))
print(discount_price(price=220))
print(discount_price(price=250,discount=20))




# Q5. Why would you use a default parameter instead of just hardcoding a value inside the
# function? Explain with an example.
# def greet(name,age):
#     print("Hello!",name)
#     if age>18:
#         print("you are eligible for vote")
#     else:
#         print("you are not eligible for vote")
# greet("Ajju",20)

def greet(age,name="user"):
    print("Hello!",name)
    if age>18:
        print("you are eligible for vote")
    else:
        print("you are not eligible for vote")
greet(20)
greet(20,"aravind")
greet(age=26)
greet(age=18,name="rajesh")