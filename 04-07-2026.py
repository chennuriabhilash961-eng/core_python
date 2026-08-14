# 1 write a function multuply(a,b,c) that returns the product of three numbers
def mul(a,b,c):
    return a * b * c
print(mul(10,20,25))

# 2 create a function describe_pet(animal,name) that prints: 'My [animal] is named as[name].'
def describe_pet(animal,name):
    print("My",animal,"is named as",name)
describe_pet("Dog","scubby")

# 3 what happens if you call a function with fewer arguments than parameters? Try it and note the error
def describe_pet(animal,name):
    print("My",animal,"is named as",name)
# describe_pet("Dog")
# describe_pet() missing 1 required positional argument: 'name'

# 4 write a function power(base,exponent) that returns base raised to exponent using ** operator
def power(base,exponent):
    return base ** exponent
print(power(2,4))

# 5 create a function full_name(first,middle,last) that returns the full name as a string 
def full_name(first,middle,last):
    return first+middle+last
print(full_name("chennuri"," ","Abhilash"))

def full_name(first,middle,last):
    return first+' '+middle+' '+last
print(full_name("chennuri","","Abhilash"))

# create a function calculate bill with parameters price and quantity that returns the total cost add 40 rs delivery if total is less than 200 call in one line print
def calculate(price,quantity):
    return price*quantity
total=calculate(50,1)
print(total)
if(total<200):
    total+=40
    print(total)

def calculate(price,quantity):
    total=price*quantity
    if(total<200):
        total+=40
    return total
print(calculate(50,9))

# create a python application with three functions total with three parameters of 3 subject marks next function avg takes input of total three subjects marks create another function greater than takes avg is 85 return A grade if avg is 75 return B grade if avg is 65 to 75 return C grade if avg is 50 to 65 return D grade else return fail call it in a single line
def total(sub1,sub2,sub3):
    return sub1+sub2+sub3
s=total(73,85,92)
print(s)
def avg(s):
    return s/3
t=avg(s)
print(t)
def grade(t):
    if(t>85):
        return "A"
    elif(t>75 and t<85 ):
        return "B"
    elif(t>65 and t<75 ):
        return "C"
    elif(t>50 and t<65):
        return "D"
    else:
        return "Fail"
print(grade(t))
print(grade(avg(total(73,85,92))))

# crete a python program to develop a simple ATM system where a user attempts to withdraw money or a deposit money your application should verify it sufficient balance is available then display the remaining balance Implement this using multiple functions like deposit ,withdraw,check balance and produce the final output in a single stmt




