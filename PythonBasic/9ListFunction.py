numbers = [99,4,85,15,16,223,42]
friends = ["Kevin", "Karen", "Jim", "David", "Oscar"]

print(friends)

# Concatenate the list
friends.extend(numbers)
print(friends)

# Add more item at the end of list
friends.append("Droz")
print(friends)

# Insert more item to the list
friends.insert(1, "Kelly")
print(friends)

# Find index of item: If not found, produced error
print(friends.index("Kelly"))

# Count number of the item
print(friends.count("Jim"))

# Sort item: Sort has no return type
numbers.sort()
print(numbers)

# Reverse item
numbers.reverse()
print(numbers)

# Copying list
friends2 = friends.copy()
print(friends2)

# Remove item: Item must be in the list
friends.remove("Jim")
print(friends)

# Remove last element
friends.pop()
print(friends)

# Clear list
friends.clear()
print(friends)