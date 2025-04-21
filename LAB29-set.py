#LAB29 Set (เซต)

score = {100,50,10,5,1}

score.add("I") #เพิ่มสมาชิก "I" เข้าไปใน Set score
print(score)
score.remove("I") #ลบสมาชิก "I" ออกจาก Set score
print(score)
score.discard("I")
print(score)

score2 = set((200,100,50,25,10,5,1))
print(score2)
##score.update(("I","J","K"))

data = score.union(score2) #นำเอาสมาชิกทั้ง 2 มารวมกัน
print(data)

animal ={"หมู","หมา","วัว"}
animal1 ={"ไก่","หมู","ปลา","วัว"}
totalAnimal = animal.union(animal1)
print(totalAnimal)

color = {"แดง","ส้ม","น้ำเงิน"}
color2 = {"น้ำเงิน","เขียว","เหลือง"}
Full_Color = color.intersection(color2)
print(Full_Color)

ElectronicDevice = {"Diode","Transistor","Mosfet","IGBT"}
ElectronicDevice2 = {"Resistor","Triac","Diode","IGBT"}
total_ElectronicDevice = ElectronicDevice.difference(ElectronicDevice2)
print(total_ElectronicDevice)
