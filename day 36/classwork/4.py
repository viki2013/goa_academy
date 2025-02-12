def split_sentence(user_str):
    words = user_str.split()  # ყოფს ტექსტს სფეისების მიხედვით
    print(words)  

# მომხმარებლისგან ტექსტის მიღება
user_input = input("შეიყვანეთ წინადადება: ")

# ფუნქციის გამოძახება
split_sentence(user_input)
