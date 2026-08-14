# Arbitrary
# *args-positional arguments
# -> variable no.of positional argument
# ->variable no of keyword argument

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(10,20,30))
print(add(1,2,3,4,5))



def order_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
order_details(order_id=1234,name="abcd",cart=["biryani","lassi","cola"],bill=500,addons=True,sauce="tomato sauce",veggies=["lemons","onions"])

# Q1. Write a function multiply_all(*args) that returns the product of all numbers passed.
def multiply_all(*args):
    mul=1
    for i in args:
        mul*=i
    return mul
print(multiply_all(2,3,4))


# Q2. Create a function display_tags( ** kwargs) that prints each keyword-value pair on its
# own line.
def display_tags(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")
display_tags(age=54,name="hi",city="kphb")


def calculate_bill(*bill):
    total=0
    for i in bill:
        total+=i
    return total

def apply_insurance(amount,**insurance):
    total_claim=0
    for key,value in insurance.items():
        print(f"{key}:{value}")
        total_claim+=value
    return amount-total_claim
    
def calculate_tax(amount,**tax):
    total_tax=0
    for key,value in tax.items():
        print(f"{key}:{value}")
        total_tax+=value
    return amount+total_tax

total=calculate_bill(10000,200,500)
total=apply_insurance(total,lic=5000,star=2500)
print(calculate_tax(total,sgst=100,gst=200))

