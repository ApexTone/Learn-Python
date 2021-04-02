score = int(input())
mid = int(input())
final = int(input())
score += mid+final

if score >= 80:
    grade = 'A'
elif score >= 75:
    grade = 'B+'
elif score >= 70:
    grade = 'B'
elif score >= 65:
    grade = 'C+'
elif score >= 60:
    grade = 'C'
elif score >= 55:
    grade = 'D+'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'
print(grade)
