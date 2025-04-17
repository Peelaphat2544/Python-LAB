#Challenge LAB20 Sum of 5 numbers (ผลรวมตัวเลข 5 ตัวเลข)

total = 0
for i in range(1,5):
    Number = int(input("กรอกตัวเลขลำดับที่ " + str(i) + " : "))
    total += Number
print("ผลรวมของ 5 จำนวน",total)