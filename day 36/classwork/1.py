def check_lowercase(user_str):
    if user_str.islower():
        print(user_str)
    else:
        print("ტექსტი არ არის მთლიანად lowercase-ში.")

# მომხმარებლისგან ტექსტის შეყვანა
text = input("შეიყვანეთ ტექსტი: ")

# ფუნქციის გამოძახება
check_lowercase(text)