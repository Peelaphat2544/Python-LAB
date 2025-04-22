#Pattern Matching (mapping pattern)
#dictionary

data = {"name":"พีลพัทร์", "type":"member"}

match data:
    case {"type" :"member"} :
        print("คุณคือสมาชิก",f"ที่ชื่อ {data['name']}")
    case _:
        print("คุณไม่ใช่สมาชิก")

#Advace
print("=======================================================")

customer = [
    {"name":"Jone", "type":"member"},
    {"name":"Tidy", "type":"non member"},
    {"name":"Tom", "type":"member"},
    {"name":"Jessica", "type":"member"},
    {"name":"Yun", "type":"non member"}
]

match customer :
    case {"name" :"Jone"} :
        print(f"{customer['name']}is Member")
        print("คุณได้ส่วนลด 10 %")
    case _ :
        print("คุณไม่ใช่สมาชิก")
        print("อดแดก")

#Advace2
print("=======================================================")

idCustomer = int(input("กรุณากรอกหมาเลขลำดับสมาชิกของท่าน (1-4) : "))

dataCustomer = [
    {"ชื่อ":"พี", "ประเภท":"สมาชิก"},
    {"ชื่อ":"มีน", "ประเภท":"ไม่ได้เป็นสมาชิก"},
    {"ชื่อ":"แก้ว", "ประเภท":"สมาชิก"},
    {"ชื่อ":"สา", "ประเภท":"สมาชิก"}
]

print(f"ลำดับสมาชิกของท่าน คือ {idCustomer} ข้อมูลของท่านคือ {dataCustomer[idCustomer-1]["ชื่อ"]}")
match dataCustomer[idCustomer-1]:
    case {"ประเภท":"สมาชิก"} :
        print("คุณเป็นสมาชิก รับส่วนลด 50 %")
    case _ :
        print("คุณไม่ได้เป็นสมาชิก และไม่ได้รับส่วนลด 50 %")