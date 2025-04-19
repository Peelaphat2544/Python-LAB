#LAB26 Non-Primitive Data Type (ชนิดข้อมูลแบบอ้างอิง) lish

color = ["RED","GREEN","BLUE"]
print("แสดงข้อมูลของ lish score",color)
print("แสดงข้อมูลของ lish score index 1 =",color[0])
print("แสดงข้อมูลของ lish score index 2 =",color[1])
print("แสดงข้อมูลของ lish score index 3 =",color[2])
print("แสดงข้อมูลของ lish score index -1 =",color[-1])
print("แสดงข้อมูลของ lish score index -2 =",color[-2])
print("แสดงจำนวนสมาชิกของ lish score =",len(color))

color2 = ["Green","Yellow","Black"]
TotalColor = color+color2
print("แสดงข้อมูลของ lish TotalColor",TotalColor,"ผลรวมทั้งหมดใน lish TotalColor =",len(TotalColor))

#ดึงข้อมูลสมาชิกใน Lish
print(TotalColor[:2])
print(TotalColor[0:2])
print(TotalColor[2:7])

#แก้ไขตำแหน่งข้อมูลใน Index lish
TotalColor[0]="K"
print(TotalColor)

#เข้าถึงข้อมูลสมาชิกด้วย loop
for checkColor in TotalColor:
    print(checkColor)