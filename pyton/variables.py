# Your First Python Code: Working with Variables

# 1. Print a friendly greeting
#print("Hello, World!")
#print("Welcome to your first Python program!\n")

# 2. Declare some basic variables
name = "Krish"         # String (text)
age = 22               # Integer (whole number)
is_learning = True     # Boolean (True/False)
skills = ["Java", "Python"]  # List (collection)

# 3. Print the variables and their types
#print(f"User Name: {name} (Type: {type(name).__name__})")
#print(f"Age:       {age} (Type: {type(age).__name__})")
#print(f"Learning:  {is_learning} (Type: {type(is_learning).__name__})")
#print(f"Skills:    {', '.join(skills)} (Type: {type(skills).__name__})")


myname = "krish patel"
age = 23
is_goodlooking = True
skills = ["docker", "kubernetes", "aws", "terraform"]

#print(f"My Name:       {myname.title()}")
#print(f"My Age:        {age}")
#print(f"Good Looking:  {is_goodlooking}")
#print(f"My Skills:     {', '.join(skills)}")


#print(type(age))

#list
fruits = ["apple", "banana","kiwi"]

#tuple
coordinates =(10.5,12.6)

#range 
numbers = range(1,10)
#print(list(numbers))

#sets
unique = {1,2,3,4,5}
#print(unique)


for fruit in fruits:
    print(fruit)

#Strings 

name = 'Krish'

print(name[0])
print(name[-1])
print(name[::-1])