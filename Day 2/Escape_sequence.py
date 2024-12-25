"""Here we will learn about escape sequences in Python.
Escape Sequences are used to insert charcter that are illegal to print in Python.
Like, if you want to print a double or single quote in a string, you can use escape sequence.
Escapde sequences are written using a backslash "\" followed by a character.
Some of the escape sequences are: \n, \t, \', \", \\, etc."""

#-------------------------------------------------------------------------------------------------------------

# Example of escape sequence to print a single or double quote in a string.

print('I am learning about \'Escape Sequences\' in Python.')
# Output: I am learning about 'Escape Sequences' in Python.

print("I am learning about \"Escape Sequences\" in Python.")
# Output: I am learning about "Escape Sequences" in Python.

#--------------------------------------------------------------------------------------------------------------

#Example of escape sequence to print a backslash and newline in a string.

print("I am learning about \\Escape Sequences\\ in Python.")
# Output: I am learning about \Escape Sequences\ in Python.

print("I am learning about \nEscape Sequences in Python.")
# Output: I am learning about
# Escape Sequences in Python.
# The above code will print the text in two lines because of the \n escape sequence.

#--------------------------------------------------------------------------------------------------------------

#Example of escape sequence to print a tab in a string.

print("I am learning about \tEscape Sequences in Python.")
# Output: I am learning about 	Escape Sequences in Python.
