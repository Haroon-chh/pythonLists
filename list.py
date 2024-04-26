# Input
gradeItems = ("Quizzes", .30, 6, "Exams", .70, 3)
grades = (100, 95, 100, 100, 93, 95, 100, 90, 80)

# Processing
gradeOutput = []
total_weighted_average = 0

for i in range(0, len(gradeItems), 3):
    category = gradeItems[i]
    weight = gradeItems[i + 1]
    num_grades = gradeItems[i + 2]
    category_grades = grades[:num_grades]
    grades = grades[num_grades:]
    average = sum(category_grades) / num_grades
    weighted_average = average * weight
    gradeOutput.append(f"{category:10} {weight * 100:6.0f} {average:8.2f} {weighted_average:12.2f}")
    total_weighted_average += weighted_average

gradeOutput.append("---------------------------------------")
gradeOutput.append(f"Final Grade: {total_weighted_average:.2f}")

# Output
print("Category  Weight  Average  Contribution")
print("---------------------------------------")

for i in range(len(gradeOutput) - 1):
    print(gradeOutput[i])

print("---------------------------------------")
print(gradeOutput[-1])
