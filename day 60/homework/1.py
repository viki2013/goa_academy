#1
name = ["lizi" , "viki" , "daviti" , "nika"]
try:
    user=int(input("enter number"))
    print(name[user])

except ValueError:
    print("wrong value")

except IndexError:
    print("wrong index")

#2
try:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    print(f"sum of numbwrs {num1} and {num2} is {num1+num2}")
except ValueError:
    print("wrong number")

#3
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 / num2
    print("Result of division: ")
except ZeroDivisionError:
    print("Error")
except ValueError:
    print("Error: Please enter numeric values.")

# 4
string_input = input("Enter a string ")

try:
    converted = int(string_input)
    print("Converted integer:")
except ValueError:
    print("Error")
