name = input("Enter student name: ")
score = int(input("Enter score: "))

if score >= 50:
    status = "Pass"
else:
    status = "Fail"

print("Student:", name)
print("Score:", score)
print("Status:", status)