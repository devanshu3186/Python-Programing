'''
In python, we can take user input directly by using input() function.
This input function gives a return value as string/character hence we have to pass that into a variable.
'''
a=input("Enter you name: ")
print("Your name is:",a)

#But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

n1=(input("Enter First number: "))
n2=(input("Enter Second number: "))
c=n1+n2
print("The sum of",n1,"+",n2,"is:",c)


n1=int(input("Enter First number: "))
n2=int(input("Enter Second number: "))
c=n1+n2
print("The sum of",n1,"+",n2,"is:",c)