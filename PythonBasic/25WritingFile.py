# Append mode
employee_file = open("25WritingFile_Employees.txt", "a")

# Write/Append to file
employee_file.write("\nToby - HR")
employee_file.write("\nKelly - Customer Service")

employee_file.close()


# Write mode
employee_file = open("25WritingFile_Employees.txt", "w")

employee_file.write("Toby - HR")
employee_file.write("\nKelly - Customer Service")

employee_file.close()

# Create new file
employee_file = open("25WritingFile_NewFile.txt","w");
employee_file.write("This is a new file")
employee_file.close()