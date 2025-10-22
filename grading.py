#python student grading system
def get_grade(percentage):
    """
    Returns the grade based on the percentage.
    
    Parameters:
    percentage (float): The student's percentage.
    
    Returns:
    str: The grade corresponding to the percentage.
    """
    if 90 <= percentage <= 100:
        return "Grade A"
    elif 80 <= percentage < 90:
        return "Grade B"
    elif 70 <= percentage < 80:
        return "Grade C"
    elif 60 <= percentage < 70:
        return "Grade D"
    else:
        return "Grade F"

def main():
    # Accept student details
    name = input("Enter the student's name: ")
    
    # Validate if name contains only letters and spaces
    while not all(char.isalpha() or char.isspace() for char in name):
        print("Please enter a name containing only letters and spaces.")
        name = input("Enter the student's name: ")
    
    roll_number = input("Enter the student's roll number: ")
    
    # Accept marks in 5 subjects
    subjects = ["Mathematics", "Science", "English", "History", "Geography"]
    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Calculate total marks and percentage
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    
    # Determine the grade
    grade = get_grade(percentage)
    
    # Store student details in a dictionary
    student_details = {
        "Name": name,
        "Roll Number": roll_number,
        "Marks": dict(zip(subjects, marks)),
        "Total Marks": total_marks,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }
    
    # Print student details
    print("\nStudent Details:")
    for key, value in student_details.items():
        if key == "Marks":
            print(f"{key}:")
            for subject, mark in value.items():
                print(f"  - {subject}: {mark}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
