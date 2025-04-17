#Challenge Grade Evaluation
'''
Score Mark
A+ = 80 - 100
A = 75 - 79
B+ = 70 - 74
B = 65 - 69
C+ = 60 - 64
C = 55 - 59
D = 50 - 54
F = 0 - 49
'''
score = int(input("กรุณาป้อนคะแนนของคุณ : "))
print("คะแนนของคุณคือ",score)
grade = None

if score >= 80 and score <= 100 :
    grade = "A+"
elif score >= 75 and score <= 79 :
    grade = "A"
elif score >= 70 and score <= 74 :
    grade = "B+"
elif score >= 65 and score <= 69 :
    grade = "B"
elif score >= 60 and score <= 64 :
    grade = "C+"
elif score >= 55 and score <= 59 :
    grade = "C"
elif score >= 50 and score <= 54 :
    grade = "D"
elif score >= 0 and score <= 49 :
    grade = "F"
else:
    grade = "คะแนนไม่ถูกต้อง"

print("เกรดของคุณคือ",grade)