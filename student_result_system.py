for i in range(3):
    name = input("Enter student name: ")
    score = int(input("Enter score: "))

    if score >= 50:
        status = "Pass"
    else:
        status = "Fail"

    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print("\nStudent:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("Status:", status)