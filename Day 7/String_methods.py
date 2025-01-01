a="Devanshu KuMar!!!"
b=" "
'''Strings are immutable in python, which means that once a string is created, it cannot be changed.
However, you can assign a new value to the same variable name. Here a new copy of the string is created and the old one is discarded using string methods.'''
print(len(a)) #prints the length of the string
print(a.upper()) #converts all characters in upper case
print(a.lower()) #converts all character to lower case
print(a.strip()) #removes any whitespace from the beginning or the end
print(a.rstrip('!')) #remove all the trailing characters from the right end 
print(a.lstrip('D')) #remove all the leading characters from the left end
print(a.replace("Kumar","Don")) #replaces a string with another string
print(a.split(" ")) #splits the string into substrings if it finds instances of the separator
print(a.capitalize()) #converts the first charater to upper case, and the rest to lower case 
print(a.center(50)) #returns a centered string of length width 
print(a.count("a")) #returns the number of times a specified value occurs in a string
print(a.endswith("!!!")) #returns true if the string ends with the specified value else false
print(a.startswith("Dev")) #returns true if the string starts with the specified value else false
print(a.startswith("Dev",0,7)) #returns true if the string starts with the specified value else false
print(a.find("a")) #searches the string for a specified value and returns the position of where it was found first and -1 if not found
print(a.index("ev")) #searches the string for a specified value and returns the position of where it was found first and throws an error if not found
print(a.isalnum()) #returns true if all characters in the string are alphanumeric else false
print(a.isalpha()) #returns true if all characters in the string are in the alphabet else false
print(a.islower()) #returns true if all characters in the string are in lower case else false
print(a.isupper()) #returns true if all characters in the string are in upper case else false
print(a.isprintable()) #returns true if all characters in the string are printable else false
print(b.isspace()) #returns true if all characters in the string are whitespaces else false
print(a.istitle()) # Returns True if all words in a text start with a upper case letter, and the rest of the word are lower case letters, otherwise False.
print(a.title()) #Converts the first character of each word to upper case and the rest to lower case
print(a.swapcase()) #Swaps cases, lower case becomes upper case and upper case becomes lower case