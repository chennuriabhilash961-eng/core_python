def hi(name,age,gender="undisclosed",*hobbies,**details):
    print("Hi",name)
    print("Your age is:",age)
    print("Your gender is:",gender)
    print("Your hobbies are:")
    for hobby in hobbies:
        print(hobby)
    print("Your details are:")
    for key,value in details.items():
        print(key,":",value)
hi("abhilash",23,"male","reading books","watching movies","playing games",skills=['python','sql',"java"],college="Trinity college",code="TCTK")

# create a python appn to design a function for a food delivery appn where the customer name is taken as positional argument and order type is default argument with default value regular the funcyion should accept the multiple food items ordered by the customer using positional argument and additional details such as address payment mode ,delivery instructions and discount using keyword argument the function should display the complete order summary including customer details list of items ordered total no of items and all additional information
def food_delivery(customer_name,order_type="regular",*food_items,**details):
    print("Customer name is:",customer_name)
    print("order type is:",order_type)
    print("food items are:")
    for food in food_items:
        print(food)
    print("total food items:",len(food_items))
    print("Additional details are:")
    for key,value in details.items():
        print(key,":",value)
food_delivery("Hari","zomato","burger","pizza","shawarma",address="2-51,kphb",payment_mode=["upi","cash","card"],delivery_instruction="Be on time",discount=20)


# Design a Python program for a supermarket billing system. Create a function calculate_total(*prices) that accepts the prices of multiple items and returns their total cost. Then define a function apply_discount(*amount) that applies a 10% discount if the total exceeds 1500. Finally, create a function final_bill(**details) that accepts keyword arguments such as amount, tax, and packing_charge, and returns the final payable bill. Display the final amount using a single nested function call.
def calculate_total(*prices):
    total=0
    for price in prices:
        total+=price
    return total
def apply_discount(*amount):
    total=amount[0]
    if total>1500:
        return total-total*0.1
    return total
def final_bill(**details):
    total_bill=0
    for key,value in details.items():
        print(key,":",value)
        total_bill+=value
    print("Total bill",total_bill)




final_bill(total_bill=apply_discount(calculate_total(int(input("Enter first item price:")),int(input("Enter second item price:")),int(input("Enter third item price:")))),sgst=100,gst=200,packing_charge=50,shipping_charge=50)

