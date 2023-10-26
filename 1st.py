def calculate_totals_and_averages(marks):
    num_students = len(marks)
    student_totals = [sum(marks[i]) for i in range(num_students)]
    subject_averages = [sum(marks[i][j] for i in range(num_students)) / num_students for j in range(5)]

    return student_totals, subject_averages

num_students = int(input("Enter the number of students: "))
marks = []
for i in range(num_students):
    print(f"Enter marks for Student {i + 1}:")
    student_marks = [int(input(f"Subject {j + 1}: ")) for j in range(5)]
    marks.append(student_marks)


student_totals, subject_averages = calculate_totals_and_averages(marks)

print("Total marks of each student:")
for i, total in enumerate(student_totals):
    print(f"Student {i + 1}: {total}")

print("\nAverage marks of each subject:")
for j, average in enumerate(subject_averages):
    print(f"Subject {j + 1}: {average:.2f}")
