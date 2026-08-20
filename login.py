# login
sa=0
usa=0
user="vamc"
pwd="0795"
def dec(func):
    def wrap(*args,**kwargs):
        print("Application started")
        func(*args,**kwargs)
    return wrap
@dec
def login(username,password):
    global sa,usa
    if(username==user and password==pwd):
        sa+=1
        print("Login successful")
    elif(username!=user):
        usa+=1
        if(usa<=3):
            x=input("Enter username:")
            login(x,password)
        else:
            print("No more attempts")
    else:
        usa+=1
        if(usa<=3):
            x=input("Enter password")
            login(username,x)
        else:
            print("No more attempts")
login("Abhi","1133")
print(sa)
print(usa)

