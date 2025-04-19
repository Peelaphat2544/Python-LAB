#LAB27 list function (ฟังก์ชันจัดการลิสต์)

colors = ["red","green","blue"]
print(colors)
print()
colors.append("yellow") #เพิ่มสมาชิกในลิส
print(colors)
print()
colors.extend(["black","gray"]) #เพิ่ม list ["black","gray"]
print(colors)
print()
colors.insert(2,"yellow") #แทรก yellow ใน Index ที่ 2
print(colors)
print()
print(colors.count("yellow")) #นับสมาชิก yellow
print()
colors.remove("yellow") #ลบ yellow
print(colors)
print()
colors.clear() #ลบข้อมูลในลิส
print(colors)
print()

colors1 = ["red","green","blue"]
colors1.sort() #เรียงลำดับข้อมูล
print(colors1)
colors1.reverse() #กลับลำดับข้อมูล
print(colors1)

number = [5,2,1,4,3]
number.sort() #เรียงลำดับข้อมูล
print(number)
number.reverse() #กลับลำดับข้อมูล
print(number)