# 'r'ead: just read,
# 'w'rite: overwrite file,
# "r+": read and write
# 'a'ppend: add new data

# Open file
employee_file = open("24ReadingFile_Employees.txt", "r")

# Tell if the file is readable or not (by mode and file properties)
print(employee_file.readable())

# Read entire file and pass cursor to next line
print(employee_file.read())
employee_file.close()


employee_file = open("24ReadingFile_Employees.txt", "r")
# Read line and pass cursor to next line
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

employee_file = open("24ReadingFile_Employees.txt", "r")
# Read line to array and pass cursor to nextline
print(employee_file.readlines())
employee_file.close()

employee_file = open("24ReadingFile_Employees.txt", "r")
# Random access
print(employee_file.readlines()[2])

# Always close file when done
employee_file.close()



