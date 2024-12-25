'''Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, 
salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. 
In Python, a variable's type is determined by the value assigned to it. The type of a variable can change at runtime.'''

a=10                   # Numeric variable
b=True                 # Boolean variable
c=[1,2,3,"Devanshu"]   # Sequence Variables
d="Hello"              # String variable
e=None                 # None type variable
f={1,2,3,}             # Set variable
g=(8,3,5)              # Sequence Variables
h={"Name":"Devanshu"}  # Mapping Variables
i=complex(3,5)         # Numeric variable
j=12.23                # Numeric variable
               
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h["Name"])
print(i)
print(j,"\n")

# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))

#There are mainly 5 types of data type in python, I.e:

# 1. Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i

# 2. Text data: str
# str: "Hello World!!!", "Python Programming"

# 3. Boolean data:
# Boolean data consists of values True or False.

# 4. Sequenced data: list, tuple
"""
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. 
Lists are mutable and can be modified after creation.
"""

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
# Output:[8, 2.3, [-4, 5], ['apple', 'banana']]

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

# Example:
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
# Output:(('parrot', 'sparrow'), ('Lion', 'Tiger'))

# 5. Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

# Example:
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
# Output:{'name': 'Sakshi', 'age': 20, 'canVote': True}

