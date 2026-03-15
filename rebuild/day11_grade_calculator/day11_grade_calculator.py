import csv

students = []

num_students = int(input("How many students? "))

for s in range(num_students):

    name = input("\nEnter student name: ")
    grades = []

    num_subjects = int(input("How many subjects? "))

    for i in range(num_subjects):

        while True:
            grade = float(input(f"Enter grade for subject {i+1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Grade must be between 0 and 100.")

    average = sum(grades) / len(grades)

    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"

    students.append([name, round(average, 2), letter])

print("\n=== Results ===")

for student in students:
    print(f"{student[0]} | Avg: {student[1]} | Grade: {student[2]}")

with open("grades.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Average", "Letter Grade"])

    writer.writerows(students)

print("\nGrades saved to grades.csv")