def find_minimum(user_list):
    minimum = user_list[0]  
    for num in user_list:
        if num < minimum:
            minimum = num  
    print(minimum)

# ფუნქციის გამოძახება ხუთჯერ, სხვადასხვა სიებით
find_minimum([3, 1, 4, 1, 5, 9])
find_minimum([10, 20, 5, 30, 40])
find_minimum([-3, -1, -7, -5])
find_minimum([-100, 50, 25, 75])
find_minimum([0, 2, -62, 8, -38])
