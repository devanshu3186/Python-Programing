num=int(input("enter the number:"))
match num:
    case 1 :
        print("One")
    case 2 :
        print("Two")
    case 3 :
        print("Three")
    case 4 :
        print("Four")
    case 5 if num%2==0:
        print("Five")
    case 6 if num%2==0:
        print("Six")
    case _:
        print("Invalid number")    

