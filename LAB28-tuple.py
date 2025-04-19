#LAB28 Tuple (เปลี่ยนแปลงข้อมูลไม่ได้)

colors = ("red","green","blue")
print(colors[1])#การเข้าถึงสมาชิก
print(colors[:3])
print(colors[1:3])
print(len(colors))

for item in colors:
    print(item)

Product = tuple(("X",5,True))
print(Product)

Position, value, isvalue = Product #การกระจายข้อมูล
print(Position)
print(value)
print(isvalue)

colors1 = ("red","green","blue")
colors2 = ("pink","black","white")

full_colors = colors1 + colors2 #เชื่อมต่อ tuple
print(full_colors)
print(full_colors*2) #ทำซ้ำ Tuple
print(full_colors*3) #ทำซ้ำ Tuple

print(full_colors.index("red")) #ค้นหาตำแหน่ง Index
print(full_colors.count("red")) #นับจำนวนค่า red ใน tuple