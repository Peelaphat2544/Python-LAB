#LAB12 Ternary Operator if..else
number = int(input("กรุณาป้อนตัวเลขของคุณ : "))
print("ตัวเลขของคุณคือ",number)

if number%2 == 0 :
    print("เป็นเลขคู่")
else:
    print("เป็นเลขคี่")

#Terary Operator if..else
print("")

print("เป็นเลขคู่") if number%2 == 0 else print("เป็นเลขคี่")