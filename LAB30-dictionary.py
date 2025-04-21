#LAB30 dictionary

color = {"แดง":"red","ส้ม":"orange","น้ำเงิน":"blue"}
print(color)
print("เรียกสีแดงภาษาอังกฤษมาใช้",color["แดง"])
print("เรียกสีส้มภาษาอังกฤษมาใช้",color["ส้ม"])

color["เหลือง"]="yellow"
print(color)

color["น้ำเงิน"]="skyblue"
print(color)

confirm = {
    True:"ตกลง",
    False:"ไม่ตกลง"
}

print(confirm[True])
print(confirm[False])


number={
    "เลขคู่":[2,4,6,8,10],
    "เลขคี่":[1,3,5,7,9]
}

print(number["เลขคู่"])
print(number["เลขคี่"])

#ฟังก์ชันจัดการ Dictionary

Month = {
    1:"มกราคม",
    2:"กุมภาพันธ์",
    3:"มีนาคม",
    4:"เมษายน",
    5:"พฤษภาคม",
    6:"มิถุนายน",
    7:"กรกฎาคม",
    8:"สิงหาคม",
    9:"กันยายน",
    10:"ตุลาคม",
    11:"พฤศจิกายน",
    12:"ธันวาคม"
}
print()
print(Month.keys()) #แสดง Key
print(Month.values()) #แสดง Value
print(Month.items()) #แสดง item
print()

for key in color.keys():
    print(key)
print()
for value in color.values():
    print(value)
print()
for key,value in color.items():
    print(key,"=",value)

Month.pop(1) #ลบข้อมูลใน Dictionary
#Month.clear() #ลบข้อมูลใน Dictionary ทั้งหมด

for key,value in Month.items():
    print(key,"=",value)

Month.update({1:"มกคราคม"}) #เพิ่มและแก้ไขข้อมูล

for key,value in Month.items():
    print(key,"=",value)
