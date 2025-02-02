 correct_password = "Goa best"
attempts = 0

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted!")
        
    else:
        attempts += 1
        print("Incorrect password. Try again.")

print("Number of incorrect attempts:"+ str(attempts))
