total = 0
highest = 0
lowest = 100

for i in range(3):
    score = int(input("Enter score: "))

    total = total + score

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

average = total / 3

print("Highest =", highest)
print("Lowest =", lowest)
print("Average =", average)