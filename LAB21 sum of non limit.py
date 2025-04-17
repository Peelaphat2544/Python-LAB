#Challenge LAB21 Sum of Non Limit (รวมจำนวนตัวเลขไม่จำกัดจำนวน)
total = 0
while True:
    number = int(input("ป้อนตัวเลข : "))
    if number <= 0:
        print("****หยุดเพื่อรวมผลลัพธ์****")
        break
    total += number
print("ผลรวมเป็น : ", total)