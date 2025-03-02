numbers = [3, 7, 2, 9, 5]

def find_max_loop(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print("მაქსიმალური რიცხვი (ციკლით):" )