highest = 0

for i in range(3):
    score = int(input("Enter score: "))

    if score > highest:
        highest = score

print("Highest score =", highest)