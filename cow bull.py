import random
list1=[1,2,3,4,5,6,7,8,9]
list2=random.sample(list1,4)
attempts=9
list3=[]
list4=[]
i=1
while i<attempts:
    number=int(input("enter number"))
    position=int(input("enter the position"))
    if (number in list2) and (list2.index(number)==position):
        list3.insert(position,number)
        print("bull",list3)
    elif (number in list2) and (list2.index(number)!=position):
        list4.append(number)
        print("cow",list4)
    i+=1
if list3==list2:
    print("congrats")
else:
    print("u loss")