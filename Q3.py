students = int(input("Number of students: "))
days = int(input("Number of days: "))

names = []
attendance = []

for i in range(students):
    name = input("Student name: ")
    data = input("Attendance (comma-separated): ")

    names.append(name)
    attendance.append(list(map(int, data.split(","))))

for day in range(days):
    present_students = []

    for student in range(students):
        if attendance[student][day] == 1:
            present_students.append(names[student])

    print(f"Day {day + 1}: {present_students}")