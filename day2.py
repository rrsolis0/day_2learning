# # Description: This file is for the second day of the python workshop


# # create variables for the following :
# # 1. age
# age = 16
# # 2. name
# name = "Ruby"
# # 3. song
# song = "Happy Birthday"
# # 4. food
# food = "pizza"
# # 5. number
# number = 100
# # #now include the variables you just made print in the following...
# print(f'''Once upon a time, there was a {age} old coder named  {name}.
#  {name} liked to hum the song {song} while coding. It was so annoying that their teammates would throw {food} until {name} would stop singing.
# Still, {name} was the best coder on the team and could write {number} lines of code every day.
# Maybe {song} was {name}s secret power?
# No one will ever know.''')

# #f string inerpolation is a way to format strings in python.
# # It allows you to use varibles inside of strings.
# # What is syntax ? What is an algorithm? a way of writing code that is correct and follows the rules of the languge python
# # a set of intrsution that are followed to solve a problem 
# # what is a variable? What is a string?
# #varibles hold data
# #name = "John" #javascript syntax
# #age = is undifined because it has no value 
# # strings are nothing but plain text
# # what does this do?
# print("Giraffe \n academy")
# # /n makes a new laugh 
# print("Giraffe \t academy")
# # \t makes a tab







# # or this
# phrase = "python learning"
# print(phrase + "is cool")
# #this is called concatenation or string interpolation
# #what does the + sign do? What is it called? 


# #what if I wanted to get the length of a phrase?
# print(f'the length of the phrase" {len(phrase)}')
# declartionOfIndependence="We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed,—That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.—Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world.."
# #find the length of the declartion of idnepedence 
# #the declarationOfIdependence = str(declartionOfIndependece)
# print(f'len(declartionOfIndependence)')
# #len allows you to find the lenght of a string


#what if I wanted to make the letters in the variable upper case or lower?
new_phrase = "welcome to day 2 part 3"  
print(len(new_phrase))
print(new_phrase.upper())
#.upper is a method that makes the string all upper case
#parentheses are used to call methods
print(new_phrase.lower())
#.lower is a method that makes the string all lower case

#what if I wanted to check and see if the phrase was all lower or upper?
print(new_phrase.islower())

#What if I wanted to get one letter of the phrase
print(new_phrase[0]) # prints the first letter 
print(new_phrase[1])#prints the second letter
print(new_phrase[2])#prints the 3 letter
print(new_phrase[11])
#get the last letter of the prhase
print(new_phrase[-1])

# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase
# letter eye) as single character variable names.



# Working with numbers bold text
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Addition
print(2 + 2)

# Subtraction
print(2 - 5)

# Multiplication
print(2 * 3)

# Division
print(10 / 2)

# Modulus
print(10 % 3)# 10 is divided by 3 is 3 with a remainder of 1

# Exponentiation
print(2 ** 3)# 2 to the power of 3

# Floor Division
print(10 //3)# 10 is divided by 3 is 3 with a remainder of 1

# Order of Operations followed in Python
print(2 * 3 + 1)#7
# You can use parentheses to specify the order in which you want operations to be performed.

#to do more you need to import special math libraries from python
#from math import *
#this goes out and grabs some different math functions we can use
#floor method
#ceil method
#sqrt method
from math import * #import everything
print(floor(95.76666))
print(ceil(98.3333))
print(sqrt(54))


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers. Integers are just whole numbers,
# positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or
# use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of
# floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating
# point number in Python.



# challenge exerces... 
#create a program that asks for the user's name and age and then prints out the user's name and age

# create a program that asks for the user's name and then prints out the user's name in all caps

# create a program that asks for the user's name and then prints out the user's name in all lower case

# create a program that asks for price and then prints out the price with a 10% discount

# Given the phrase "Hancock High School", perform the following operations:
# Print the phrase with a newline character to separate "Hancock" and "High" and "School".
# Concatenate the phrase with " is cool", and print the result.
# Print the length of the phrase.
# Convert and print the phrase in uppercase and lowercase.
# Check if the phrase is all lower or all upper and print the result.
# Print the first and the last letter of the phrase.