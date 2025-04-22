# Main Programe
'''
import calculator #นำทุกฟังก์ชันจากไฟล์ calculator.py มาใช้ในโปรแกรม Main หลักทั้งหมด
print(calculator.add(10,20))
print(calculator.sub(10,20))
print(calculator.mul(10,20))
'''
'''
import calculator as mycal #นำทุกฟังก์ชันจากไฟล์ calculator.py มาใช้ในโปรแกรม Main หลักทั้งหมด และตั้งชื่อใหม่โดยใช้คำสั่ง as
import database as db
print(mycal.add(10,20))
print(mycal.sub(10,20))
print(mycal.mul(10,20))

print(db.name) #เข้าถึงชื่อฐานข้อมูล
db.insert()
db.delete()
db.update()
'''

'''
from calculator import add as plus,sub #นำเฉพาะชื่อฟังชัน add ในไฟล์ calculator.py มาใช้งานเท่านั้น
print(plus(10,20)) #ตั้งชื่อ plus แทน add
print(sub(10,20))
'''
from calculator import * #นำทุกฟังก์ชันจากไฟล์ calculator.py มาใช้งาน
from database import * #นำทุกฟังก์ชันจากไฟล์ database.py มาใช้งาน
print(add(10,20))
insert()