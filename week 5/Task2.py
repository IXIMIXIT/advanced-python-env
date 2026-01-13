import json

def process_student_grades():
    # Step 1: Create the initial students.json file
    initial_data = [
        {"name": "Alice", "age": 20, "grades": [85, 90, 92]},
        {"name": "Bob", "age": 22, "grades": [78, 80, 70]},
        {"name": "Charlie", "age": 21, "grades": [95, 100, 98]}
    ]

    with open('students.json', 'w') as f:
        json.dump(initial_data, f, indent=4)
    print("Created students.json")

    # Step 2: Read, calculate average, and write to new file
    with open('students.json', 'r') as f:
        students = json.load(f)

    # Process each student
    for student in students:
        grades = student['grades']
        if grades:
            average = sum(grades) / len(grades)
            # Rounding to 2 decimal places for cleanliness
            student['average_grade'] = round(average, 2)
        else:
            student['average_grade'] = 0

    # Step 3: Write to a NEW file (preserving the original)
    with open('students_processed.json', 'w') as f:
        json.dump(students, f, indent=4)
    
    print("Processed data saved to students_processed.json")

if __name__ == "__main__":
    process_student_grades()