''' TODO
7. Average it out of the value of the assignment (ex. Quiz 3 worth 5 points and I got 2 so 2/5 = 40%)
9. Store all the values and averages
10. Loop until finished and requiring final grade
11. Add up ALL the weight given divided by the grade.
12. Output above ^. Show as % and as fraction
'''
print("Welcome to the grade calculator!")

grades = {}
dict = grades.items()

while True:
    assignment = input("Enter the name of the assignment: ")
    total_weight = float(input("Enter the weight of this assignment: "))
    grades[assignment] = {"Weight": total_weight}

    score = float(input("What grade did you get for this assignment?: "))
    grades[assignment]["Score"] = score

    addmore = input("Would you like to add more grades? (Y/N): ")
    if addmore.lower() == "y":
        continue
    elif addmore.lower() == "n":
        break

final_weight = 0
total_score = 0


for assignment, info in grades.items():
    weight = info["Weight"]
    score = info["Score"]
    final_weight += weight
    total_score += (score * weight) / 100

final_grade = (total_score / final_weight) * 100
print(f"\nYour total weighted average is: {round(final_grade, 2)}%")
