def calculate_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'


students = {}

try:
    num_students = int(input("Enter number of students: "))
    if num_students <= 0:
        raise ValueError("Number of students must be greater than 0.")

    for i in range(num_students):
        print(f"\nStudent {i + 1}")
        name = input("Enter student name: ")
        score = float(input("Enter student score (0–100): "))
        grade = calculate_grade(score)
        students[name] = {"score": score, "grade": grade}

except ValueError as ve:
    print("Input error:", ve)

except KeyboardInterrupt:
    print("\nProcess interrupted by user.")

finally:
    print("\n=== Grade Report ===")
    for name, info in students.items():
        print(f"{name}: Score = {info['score']}, Grade = {info['grade']}")
    print("End of Report.")
