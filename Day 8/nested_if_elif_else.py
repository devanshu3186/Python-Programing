num=int(input("Enter a number:"))
if(num>0):
    print("Number is positive")
    if(num>5):
        print("Number is greater than 5")
    else:
        print("Number is less than 5")
elif(num==0):
    print("Number is zero")
else:
    print("Number is negative")