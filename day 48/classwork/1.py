def past(h, m, s):
    new_h = 3600
    new_m = 60
    res = (new_h + new_m + s) * 1000
    return res

def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    return name + " does not play banjo"

def simple_multiplication(number):
    if number%2 == 0:
        return number
    return number


def grow(arr):
    prod = 1
    for i in arr:
        prod = prod * i

def smash(words):
    return " ".join(words)

def find_average(numbers):
    if len(numbers) == 0: return 0
    return sum(numbers) / len(numbers)

def invert(lst):
    res = []

    for i in lst:
        res.append(i*-1)

    return res

def find_needle(haystack):
    res = haystack.index("needle")
    return "found the needle at position " + str(res)