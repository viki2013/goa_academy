#Convert a String to a Number!
def string_to_number(s):
    return int(s)

#Grasshopper - Summation
def summation(num):
    result=0
    for i in range(1,num+1):
        result=result+i
    return  result

#Function 1 - hello world
def greet():
    return "hello world!"

#Remove String Spaces
def no_space(x):
    result = ""
    for i in x:
        if i != " ":
            result += i
    return result

#You Can't Code Under Pressure #1
def double_integer(i):
    return i*2

#returning string
def greet(name):
    return f"Hello, {name} how are you doing today?"

#convert a boolearn to a string
 def boolean_to_string(b):
    return str(b)

def boolean_to_string(b):
    if b == True: return "True"
    return "False"

#Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "":
        return value1 value2
    else:
        return value1 / value2

#Keep Hydrated!
def litres(time):
    return int(time*(0.5))

#Century From Year
def liters(time):
    return int(time * 0.5)

#Convert number to reversed array of digits
def digitize(n):
    str_number = str(n)
    rev_number = str_number[::-1]

    new_list = []
    for number in rev_number:
        new_list.append(int(number))

    return new_list