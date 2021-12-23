import json
import os
dic={}
choose= int(input("choose 1. for sign up or 2. for log in"))
if choose==1:
    name=input("enter your name")
    print(name)
    password=input("enter your password (password should conatain Upper,Small Letter, Special Character and number)=")
    u,d,l,s=0,0,0,0
    for check in password:
        if len(password)>=8:
            if (check.isupper()):
                u+=1
            if (check.isdigit()):
                d+=1
            if (check.islower()):
                l+=1
            if(check=='@'or check=='$' or check=='_' or check=='#'):
                s+=1
    if (l>=1 and u>=1 and s>=1 and d>=1):
        password2=input("enter your password again")
        if password==password2:
            print("Congracts",name,"You are signed up Succesfully")
            description=input("Enter your Description")
            birth_date=input("enter Your Date Of Birth")
            Gender=input("enter your Gender")
            hobbies=input("Enter Your hobby")
        dic["description" ]=description
        dic["d_o_b"]=birth_date
        dic["Gender"]=Gender
        dic["Hobbies"]=hobbies
        dic["Username"]=name
        dic["Password"]=password
        with open("details.json","w") as f:
            f.write(json.dumps(dic, indent=2))
elif choose==2:
    user_name=input("enter your username=")
    password_5=input("enter your Log in Password=")
    with open("details.json","r") as file:
        python=json.load(file)
        if user_name==python and python==password_5:
            print("user name")
            print("gender")
            print("description")
            print("d_o_b")

        else:
                print("Password and same")            






            



