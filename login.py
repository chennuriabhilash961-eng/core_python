sa=0
usa=0
username="Abhilash"
password="9618"

def dec(func):
    def wrap(*args,**kwargs):
        print("Application Started")
        func(*args,**kwargs)
    return wrap
@dec
def login(username1,password1):
    if(username1==username and password1==password):
        global sa
        sa+=1
        print("Login successful")
    else:
        global usa
        usa+=1
        if(usa>=3):
            print("3 attempts completed")
        else:
            print("Try again")
login(input(),input())
login(input(),input())
login("Abhi","1324")
login("Abhi","1324")
print(usa)
login("Abhilash","9618")


