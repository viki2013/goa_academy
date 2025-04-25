#1
def rental_car_cost(d):
    if d >= 7: return d*40 - 50
    elif d >= 3: return d*40 - 20
    else: return d*40


#2
def quarter_of(month):
    if month <= 3: return 1
    elif month <= 6: return 2
    elif month <= 9: return 3
    return 4

#3
def remove_exclamation_marks(s):
    res = ""
    
    for i in s:
        if i != "!": res += i
        
    return res

#4
def get_volume_of_cuboid(length, width, height):
    return length * width * height

#5
def points(games):
    score = 0
    
    for game in games:
        our_score = int(game[0])
        their_score = int(game[2])
        
        if our_score > their_score:
            score += 3
        elif our_score == their_score:
            score += 1
    
    return score

#6
def greet(name):
    if name == "Johnny": return "Hello, my love!"
    return f"Hello, {name}!"

#7
def update_light(current):
    if current == "green": return "yellow"
    elif current == "yellow": return "red"
    return "green"

#8
def other_angle(a, b):
    return 180-a-b