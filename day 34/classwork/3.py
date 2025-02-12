def manual_capitalize(user_str):
    return user_str[0].upper() + user_str[1:].lower()


user_input = input("შეიყვანეთ ტექსტი: ")


print(manual_capitalize(user_input))
