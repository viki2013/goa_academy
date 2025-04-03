#1
book = {
    "Name": "harry potter",
    "fav person": "Harry",
    "Year_of_Publication": 1960,
}


#2
students_points = {
    "viki": 95,
    "daviti": 100,
    "luka": 78,
    "lizi": 92,
    "sesili": 88
}

total_points = sum(students_points.values())
average_points = len(students_points)


#3
students_grades = {
    "viki": "A",
    "sesili": "B",
    "saba": "A",
    "nika": "C",
    "erekle": "B"
}

for i in students_grades.items():
    print("Student:, Grade:" )


#4

countries_capitals = {
    "Georgia": "tbilisi",
    "Canada": "Ottawa",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}


for i in countries_capitals.items():
    print("The capital of is.")


#5
car_brands_models = {
    "Toyota": "Corolla",
    "BMW": "M3",
    "Audi": "A4"
}


print(car_brands_models["Toyota"])




