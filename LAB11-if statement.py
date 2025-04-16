#LAB11 if Statement (ถ้า)

x = int(input("ป้อนค่าตัวเลข x :"))
if x == 0 :
    print("x มีค่าเท่ากับ 0")

print("")

y = int(input("ป้อนค่าตัวเลข y :"))
if x != 5 :
    print("x มีค่าไม่เท่ากับ 5")
else:
    pass #ไม่มีการทำงานใด ๆ เกิดขึ้น ต้องการให้โปรแกรมรันได้ก่อน

print("")

z = int(input("ป้อนค่าตัวเลข z :"))
if z == 5 :
    print("Hello World")
elif z == 4 :
    print("Hello Peelaphat")
elif z == 3:
    print("Hello Python")
else:
    print("ไม่เข้าเงื่อนไข")
