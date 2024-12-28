'''In Python, anything enclosed in single or double quotation marks is considered a string. A string is a sequence of textual data. 
   Strings are used when working with Unicode characters.'''

a="My name is xyz."
print(a)

a="""Hello, my name is xyz and I am from xyz city, 
my address is xyz and my bank account number is xyz too."""
print(a)

a='''Hello, my name is xyz and I am from xyz city, 
my address is xyz and my bank account number is xyz too.'''
print(a)

a="""Hello, how's you health."""
print(a)

a='He said "I want to eat banana".'
print(a)
a="He said 'I want to eat banana'."
print(a)
# we can enclose our string in single quotes, if we want to use double quotes inside the string and vice-versa.
print(a[0])
for character in a:
    print(character)

# Above code prints all the characters in the string name one by one!