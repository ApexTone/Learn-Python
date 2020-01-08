# \n for newline like JAVA and C
print("\"A\nstring\"")

randomString = "a % ToTa\\lly raNdOm\" string"
print(randomString)
#Utility
print(randomString.upper())
print(randomString.lower())
print(randomString.isupper())
print(randomString.islower())

# Get string length
print(len(randomString))
# Random access
print(randomString[0])
# Get index of character
print(randomString.index("a"))
# Get starting index of sequence. If it's not found, error will occur
print(randomString.index("ToT"))
# Replacing all substring/character
print(randomString.replace("ToT","fww"));
