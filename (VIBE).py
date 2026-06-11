"""
Student Grade Calculator
Manages student records, calculates grades, and provides class statistics
Author: Mark Clark
Course: CIS261
Week: 10 VIBE Coding
"""

class Student:
    """Represents a student with test scores and grade information"""
    
    def __init__(self, name, student_id, test1, test2, test3):
        """Initialize a student with name, ID, and three test scores"""
        self.name = name
        self.id = student_id
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
    
    def calculate_average(self):
        """Calculate and return the average of three test scores"""
        return (self.test1 + self.test2 + self.test3) / 3
    
    def calculate_grade(self):
        """Calculate and return the letter grade based on average"""
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        """Return formatted string representation of student"""
        return f"{self.name:<20} {self.id:<10} {self.test1:>6.2f} {self.test2:>6.2f} {self.test3:>6.2f} {self.average:>7.2f} {self.grade:>5}"
    
    def to_file_format(self):
        """Return pipe-delimited format for file storage"""
        return f"{self.name}|{self.id}|{self.test1:.2f}|{self.test2:.2f}|{self.test3:.2f}|{self.average:.2f}|{self.grade}"


def load_students(filename):
    """Load student records from file"""
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split('|')
                    if len(parts) == 7:
                        name, student_id, test1, test2, test3, average, grade = parts
                        # Reconstruct student from file data
                        student = Student(name, student_id, float(test1), float(test2), float(test3))
                        students.append(student)
        print(f"✓ Loaded {len(students)} student records from '{filename}'")
    except FileNotFoundError:
        print(f"✓ No existing student file found. Starting with empty records.")
    except Exception as e:
        print(f"✗ Error loading students: {e}")
    
    return students


def save_students(students, filename):
    """Save student records to file"""
    try:
        with open(filename, 'w') as file:
            for student in students:
                file.write(student.to_file_format() + '\n')
        print(f"✓ Saved {len(students)} student records to '{filename}'")
        return True
    except Exception as e:
        print(f"✗ Error saving students: {e}")
        return False


def add_student(students):
    """Add a new student to the list"""
    print("\n--- Add New Student ---")
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("✗ Name cannot be empty")
            return
        
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("✗ Student ID cannot be empty")
            return
        
        test1 = float(input("Enter Test 1 score (0-100): "))
        if not 0 <= test1 <= 100:
            print("✗ Score must be between 0 and 100")
            return
        
        test2 = float(input("Enter Test 2 score (0-100): "))
        if not 0 <= test2 <= 100:
            print("✗ Score must be between 0 and 100")
            return
        
        test3 = float(input("Enter Test 3 score (0-100): "))
        if not 0 <= test3 <= 100:
            print("✗ Score must be between 0 and 100")
            return
        
        student = Student(name, student_id, test1, test2, test3)
        students.append(student)
        print(f"✓ Student {name} added successfully!")
        print(f"  Average: {student.average:.2f} | Grade: {student.grade}")
    
    except ValueError:
        print("✗ Invalid input. Please enter numeric values for test scores.")


def display_all_students(students):
    """Display all students in a formatted table"""
    if not students:
        print("\n✗ No student records found.")
        return
    
    print("\n" + "=" * 90)
    print(f"{'Student Name':<20} {'ID':<10} {'Test 1':>6} {'Test 2':>6} {'Test 3':>6} {'Average':>7} {'Grade':>5}")
    print("=" * 90)
    
    for student in students:
        print(student)
    
    print("=" * 90)


def calculate_class_statistics(students):
    """Calculate and display class statistics"""
    if not students:
        print("\n✗ No student records found.")
        return
    
    averages = [student.average for student in students]
    highest_avg = max(averages)
    lowest_avg = min(averages)
    class_avg = sum(averages) / len(averages)
    
    # Find students with highest and lowest averages
    highest_student = [s for s in students if s.average == highest_avg][0]
    lowest_student = [s for s in students if s.average == lowest_avg][0]
    
    print("\n" + "=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Average: {highest_avg:.2f} ({highest_student.name})")
    print(f"Lowest Average: {lowest_avg:.2f} ({lowest_student.name})")
    print("=" * 60)


def search_student(students):
    """Search for a student by name (case-insensitive)"""
    if not students:
        print("\n✗ No student records found.")
        return
    
    search_name = input("\nEnter student name to search: ").strip().lower()
    
    found_students = [s for s in students if s.name.lower() == search_name]
    
    if found_students:
        print("\n" + "=" * 90)
        print(f"{'Student Name':<20} {'ID':<10} {'Test 1':>6} {'Test 2':>6} {'Test 3':>6} {'Average':>7} {'Grade':>5}")
        print("=" * 90)
        for student in found_students:
            print(student)
        print("=" * 90)
    else:
        print(f"✗ No student found with name '{search_name}'")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("STUDENT GRADE CALCULATOR - MAIN MENU")
    print("=" * 60)
    print("1. Add new student")
    print("2. Display all students")
    print("3. View class statistics")
    print("4. Search for a student")
    print("5. Save and exit (or press ESC)")
    print("=" * 60)


def main():
    """Main program loop"""
    filename = "student_grades.txt"
    students = load_students(filename)
    
    print("\nWelcome to the Student Grade Calculator!")
    print("(Press 'ESC' or select option 5 to exit)")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5) or press ESC: ").strip().upper()
        
        # Check for ESC key (user might type "ESC")
        if choice == "ESC" or choice == "5":
            save_students(students, filename)
            print("\n✓ Thank you for using Student Grade Calculator!")
            break
        elif choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_class_statistics(students)
        elif choice == "4":
            search_student(students)
        else:
            print("✗ Invalid choice. Please enter 1-5 or ESC.")


if __name__ == "__main__":
    main()