#LAB40 Fuction (User define fuction) ฟังก์ชันที่ผุ้ใช้สร้างขึ้นมาเอง

#ฟังก์ชันพื้นฐาน
def sayHello () :
    print("สวัสดีครับ")

def showTable(): #หากไม่มีคำสั่งใด ๆ ให้ใส่ pass ไว้ก่อน
    pass

def show_Table():
    print("*********")
    for number in range(1,13):
        print(f"2 x {number} = {2*number}")

#ฟังก์ชันแบบมีพารามิเตอร์
def SayHello(name):
    print(f"สวัสดีครับ {name}")

def Show_Table(number):
    print(f"*********สูตรคูณแม่ {number}*********")
    for i in range(1,13):
        print(f"{number} x {i} = {number*i}")

def BMI(weight,height):
    bmi = weight/((height/100)**2)
    print("ดัชนีค่า BMI ของคุณคือ",bmi)

#ฟังก์ชันแบบกำหนดค่าเริ่มต้น
def saveEmployee(name,department,salary = 10000):
    print(f"ชื่อพนักงาน {name} แผนก {department} ได้รับเงินเดือน {salary} บาทต่อเดือน")

#Arguments(args,kwargs)
"""
แบบลำดับ (*args) ข้อมูลจะอยู่ในรูปแบบ Tuple ใช้เลขลำดับ (index) อ้างอิงตำแหน่งข้อมูล
แบบชื่อ (**kwargs) ข้อมูลอยู่ในรูปแบบ Dictionary ใช้ชื่อหรือคีย์อ้างอิงตำแหน่งข้อมูล
""" 
def SaveEmployee(*args) :#สร้างเป็น tuple
    print(f"ชื่อพนักงาน {args[0]} แผนก {args[1]} ได้รับเงินเดือน {args[2]} บาทต่อเดือน")
    print(f"ที่อยู่ {args[3]}")

def SaveEmployee2(**kwargs) :#สร้างเป็น dictionary แบบกำหนดชื่อ
    print(f"ชื่อพนักงาน {kwargs['name']} แผนก {kwargs['department']} ได้รับเงินเดือน {kwargs['salary']} บาทต่อเดือน")
    print(f"ที่อยู่ {kwargs['address']}")

#ฟังก์ชันแบบส่งค่ากลับ
def getCapital():
    return "กรุงเทพมหานคร"


#ฟังก์ชันรับและส่งค่า
def bmi(weight,height):
    bmi = weight/((height/100)**2)
    return bmi

def checknumber(number):
    if number%2 == 0 :
        return "เลขคู่"
    else :
        return "เลขคี่"
    
def sumation(*data):
    total = 0
    for number in data:
        total += number
    return total


#เรียกใช้ฟังก์ชัน 
userName = "นายพี บ้าบอ"
sayHello()
SayHello("นายพีลพัทร์ แก้วคง")# "นายพีลพัทร์ แก้วคง" คือ arguments 
SayHello(userName)#ตัวแปร userName คือ arguments 
show_Table()
Show_Table(5)
BMI(35,165)
saveEmployee("นายพีลพัทร์ แก้วคง","ฝ่ายบัญชี")
saveEmployee("นายพีลพัทร์ แก้วคง","ฝ่ายบัญชี",50000)
SaveEmployee("นายพีลพัทร์ แก้วคง","ฝ่ายบัญชี","123/456",50000) #arge แบบเรียงลำดับ
SaveEmployee2(name="นายพีลพัทร์ แก้วคง",department="ฝ่ายบัญชี",address="123/456",salary=50000) #แบบกำหนดชื่อ
print(getCapital())
GetCapital = getCapital()
print("เมืองหลวงของฉันคือ",GetCapital)
BMI = bmi(35,165)
print(f"ดัชนีค่า BMI ของคุณคือ {BMI:.2f}")
result = checknumber(56)
print(result)
Sumation = sumation(1,2,3,4,5,6,7,8,9,10)
print(Sumation)
