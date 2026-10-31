

#parameter argument


#Positional Arguments
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_user( 25,"Alice")

#Default Arguments

def greet(name='user'):
    print("Hello", name)

greet('sunil') # Uses passed value

def add_2_num(num1,num2=0):
    return num1+ num2

print(add_2_num(10))


# Keyword Arguments

def display_info(name, city):
    print(f"{name} lives in {city}.")

display_info(name="Ravi",city="Mumbai")