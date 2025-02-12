def iscapitalized(user_str):
    print(user_str[0].isupper() and user_str[1:].islower())

# მომხმარებლისგან ტექსტის შეყვანა
text = input("შეიყვანეთ ტექსტი: ")

# ფუნქციის გამოძახება
iscapitalized(text)
