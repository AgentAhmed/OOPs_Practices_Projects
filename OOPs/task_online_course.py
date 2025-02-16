class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []  # List of Student objects

    def enrolled_students(self, student):
        self.students.append(student)  # student should be a Student object
        print(f'{student.name} has been enrolled in {self.course} course.')    

    def course_details(self):
        print(f'Course: {self.course}')
        print(f'Instructor: {self.instructor}')  
        print(f"Enrolled Students:")  
        for student in self.students:
            print(student.name)

    def completed_course(self, name):
        for student in self.students:
            if student.name == name:  # Fix condition
                self.students.remove(student)
                print(f'{name} has completed the course.')    
                return  # Exit after removing the student
        print(f'{name} is not enrolled in this course.')  # Moved outside loop

    def avg_grade(self):
        if not self.students:
            print("No students enrolled yet.")
            return

        total_grades = sum(sum(student.grades) for student in self.students)  # Sum of all grades
        total_subjects = sum(len(student.grades) for student in self.students)  # Count of all grades
        avg = total_grades / total_subjects if total_subjects else 0
        print(f'Average grade of students is {avg:.2f}.')

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

# Get course and instructor input
course_input = input('Enter the course name: ').strip()
instructor_name = input('Enter the instructor name: ').strip()

course = OnlineCourse(course_input, instructor_name)

# Get number of students
num_students = int(input('Enter the number of students: '))

for _ in range(num_students):
    student_name = input('Enter the student name: ').strip()
    grades = [int(input(f'Enter grade {i+1}: ')) for i in range(3)]  # Collect 3 grades

    student = Student(student_name, grades)  # Create a Student object
    course.enrolled_students(student)

course.course_details()
course.avg_grade()

# Test course completion
completed_student = input("Enter the student name who completed the course: ").strip()
course.completed_course(completed_student)
