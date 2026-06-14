attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == "admin":
        print("Login successful")
        break

    attempts = attempts + 1

if attempts == 3:
    print("Account locked")