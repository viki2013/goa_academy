#1
def better_than_average(class_points, your_points):
    mean = sum(class_points) / len(class_points)
    
    if your_points > mean: return True
    return False

#2
def count_positives_sum_negatives(arr):
    if arr == [] or arr == None: return []
    
    count_of_pos = 0
    sum_of_neg = 0
    
    for i in arr:
        if i > 0: count_of_pos += 1
        else: sum_of_neg += i
    
    return [count_of_pos, sum_of_neg]

#3
def dna_to_rna(dna):
    return dna.replace("T", "U")

#4
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump: return True
    return False

#5
def bmi(weight, height):
    res = weight / height ** 2
    
    if res <= 18.5: return "Underweight"
    elif res <= 25.0: return "Normal"
    elif res <= 30.0: return "Overweight"
    return "Obese"

#6
def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)

#7
def fake_bin(x):
    num = ""
    
    for i in x:
        new = int(i)
        
        if new < 5:
            num += "0"
        else:
            num += "1"
    
    return num

#8
def string_to_array(s):
    return s.split(" ")

#9
def count_by(x, n):
    res = []
    
    for i in range(1, n+1):
        res.append(x*i)
    
    return res

#10
def reverse_seq(n):
    res = []
    
    for i in range(n, 0, -1):
        res.append(i)
    
    return res

#11
def reverse_seq(n):
    return list(range(n, 0, -1))

#12
def rps(p1, p2):
    if p1 == p2: return "Draw!"

    if p1 == "scissors":
        if p2 == "rock": return "Player 2 won!"
        else: return "Player 1 won!"
    elif p1 == "rock":
        if p2 == "scissors": return "Player 1 won!"
        else: return "Player 2 won!"
    else:
        if p2 == "scissors": return "Player 2 won!"
        else: return "Player 1 won!"


#13
def count_sheep(n):
    res = ""
    for i in range(1,n+1):
        res += f"{i} sheep..."
    return res

#14
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

