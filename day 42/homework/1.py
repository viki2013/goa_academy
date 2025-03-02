def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)


def square_sum_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0) ** 2


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of even numbers:", sum_even_numbers(numbers))
print("Square of sum of odd numbers:", square_sum_odd_numbers(numbers))