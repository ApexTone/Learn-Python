# Dictionary is a kind of structure kinda like map
# It contains 2 data, key and value
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Accessing value from key
print(monthConversion["Jan"])# Using index
print(monthConversion.get("Jan"))# Using method: Safer for bad key value
print(monthConversion.get("oct", "Default can't find fallback"))
