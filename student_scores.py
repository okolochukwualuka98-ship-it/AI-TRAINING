for i in range(3):
    name = input("Enter student name: ")
    score = int(input("Enter score: "))

    if score >= 50:
        print(name, "Pass")
    else:
        print(name, "Fail")