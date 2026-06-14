name = input("Enter student name: ")
score = int(input("Enter score: "))

if score >= 80:
    print(name, "got A")
elif score >= 70:
    print(name, "got B")
elif score>= 60:
    print(name, "got c")
elif score >= 50:
    print(name, "got D")
else:
    print(name, "got F")        