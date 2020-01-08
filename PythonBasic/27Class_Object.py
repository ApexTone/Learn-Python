# from FILE_NAME import CLASS
from Student27 import Student

# Create object
student1 = Student("John", "CE", 4.00, False)
student2 = Student("Pam", "Art", 2.33, True)

# Access attribute
print(student1.name)
print(student2.gpa)
print(student2.get_data())