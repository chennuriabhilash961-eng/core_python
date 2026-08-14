# create a function calculate bill with parameters price and quantity that returns the total cost add 40 rs delivery if total is less than 200 call in one line print
# def calculate(price,quantity):
#     total=price*quantity
#     if total<200:
#         return total+40
#     return total
# price=int(input("Enter the price:"))
# quantity=int(input("Enter the quantity:"))
# total=calculate(price,quantity)
# print(total)
# print("total bill:",calculate(int(input("Enter the price:")),int(input("enter the quantity"))))

# create a python application with three functions total with three parameters of 3 subject marks next function avg takes input of total three subjects marks create another function greater than takes avg is 85 return A grade if avg is 75 return B grade if avg is 65 to 75 return C grade if avg is 50 to 65 return D grade else return fail call it in a single line
# def total(sub1,sub2,sub3):
#     return sub1+sub2+sub3

# def avg(total):
#     return total//3

# def grade(avg):
#     if avg>85:
#         return "A"
#     if avg>75:
#         return "B"
#     if avg>65:
#         return "C"
#     if avg>50:
#         return "D"
#     return "Fail"

# sub1=int(input("Enter sub1 marks:"))
# sub2=int(input("Enter sub2 marks:"))
# sub3=int(input("Enter sub3 marks:"))
# Total=total(sub1,sub2,sub3)
# Avg=avg(Total)
# print(grade(Avg))

# print(grade(avg(total(int(input("Enter sub1 marks:")),int(input("Enter sub2 marks:")),int(input("Enter sub3 marks:"))))))


# create a python program to develop a simple ATM system where a user attempts to withdraw money or a deposit money your application should verify it sufficient balance is available then display the remaining balance Implement this using multiple functions like deposit ,withdraw,check balance and produce the final output in a single stmt
# def deposit(amount,current_balance):
#     if amount>0:
#         return amount+current_balance
#     return "Please enter a valid amount"
# def withdraw(amount,current_balance):
#     if amount>current_balance:
#         return "Insufficient funds" 
#     return current_balance-amount
# # def check_balance
# balance=int(input("Enter your balance:"))
# balance = deposit(1000,balance)
# print(withdraw(500,balance))

# print(withdraw(500,deposit(1000,int(input("Enter your balance:")))))


# Q1. Write a function intro(name, city, hobby) that prints a sentence about a person. Call it in two different orders and observe the difference.
def intro(name,city,hobby):
    print("My name is",name,"I am from",city,"My hobby is",hobby)
intro("abhi","hyd","playing cricket")
intro(city="knr",hobby="bgmi",name="ajay")

# Q2. Create subtract(a, b) that returns a - b. What is the difference between subtract(10, 3) and subtract(3, 10)?
def sub(a,b):
    return a-b
print(sub(10,3))
print(sub(b=5,a=15))

# Q3. What does 'positional' mean in 'positional arguments'? Write it in your own words.
# ->postion means the position of the argument in the parameters

# Q4. Write a function bio(first_name, last_name, age) and call it correctly using positional arguments.
def bio(first_name,last_name,age):
    print(first_name,last_name,age)
bio("chennuri","Abhi",23)

# Q5. Can you pass more positional arguments than there are parameters? What error do you get?
# -> No we cannnot pass more positional arguments than there are parameters the error is it  takes 3 positional arguments but 4 were given

# Q1. Call the function send_email(to, subject, body) using keyword arguments in any order.
def send_email(to,subject,body):
    print(to,subject,body)
send_email("abhi","for leave","I am sick")
send_email(body="I got fever",to="manager",subject="for one day leave")


# Q2. Write a function create_profile(username, email, age) and call it using keyword arguments.
def create_profile(user_name,email,age):
    print(user_name,email,age)
create_profile(age=45,user_name="abhi123",email="chennuriabhilash961@gmail.com")

# Q3. What is the error if you place a positional argument after a keyword argument? Test it.
# def create_profile(user_name,email,age):
#     print(user_name,email,age)
# create_profile(age=45,"abhi123",email="chennuriabhilash961@gmail.com")
# -> SyntaxError: positional argument follows keyword argument 

# Q4. Rewrite this call using keyword arguments: book_ticket('Alice', 'Delhi', 'Mumbai', 2)
def book_tickets(name,source,Destination,tickets):
    print(name,source,Destination,tickets)
book_tickets(name="Alice",source="Delhi",Destination="Mumbai",tickets=2)



# Q5. Why are keyword arguments considered more readable? Write an example that demonstrates this clearly.
# Keyword arguments are considered more readable because they clearly show what each value represents, without needing to remember the exact order of parameters. This makes the code easier to understand and reduces mistakes.

def book_ticket(name,source,Destination,tickets):
    print(name,source,Destination,tickets)
book_ticket(source="Delhi",tickets=2,name="Alice",Destination="Mumbai")

def learn(name,skill):
    print(name,"is learning",skill)
learn("abhi","SQL")
learn("SQL","abhi")
# Keyword arguments
learn(skill="SQL",name="Ajay")

# write a python program to build a simple uber application that has a function called trip details with parameters like driver name,pickup location,drop location,total price call this function using positional aarguments once keyword argument once
def trip_details(driver_name,pickup_location,drop_location,total_price):
    print(driver_name,pickup_location,drop_location,total_price)
# Positional Argument
trip_details("akhil","kphb","Jntu",150)
# Keyword Argument
trip_details(total_price=250,driver_name="ajju",pickup_location="JBS",drop_location="HI tech city")