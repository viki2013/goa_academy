def hello_world():
    print("Hello, World!")


def multiply_by_10(number):
    return number * 10
result = multiply_by_10(5)
print(result)  


def greet(name="Guest"):
    print("Hello!")

greet("John")  
greet() 


def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


result = find_maximum([1, 2, 3, 4, 5])
print(result)  


def positive_numbers(numbers):
    positive_list = []
    for num in numbers:
        if num > 0:
            positive_list.append(num)
    return positive_list


result = positive_numbers([-5, -2, 3, 4, -1, 7])
print(result)  

