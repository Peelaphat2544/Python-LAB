#LAB14 Nested-if (if ซ้อน if)
'''
if เงื่อนไขหลัก :
    if เงื่อนไขย่อย ที่ 1 :
         คำสั่งที่ 1
    if เงื่อนไขย่อย ที่ 2 :
         คำสั่งที่ 2
'''
#ตัวอย่าง
username = input("ป้อนชื่อผู้ใช้ : ")
password = input("ป้อนรหัสผ่าน : ")
if username == "admin" and password == "1234" :
    print("ยินดีต้อนรับเข้าสู่ระบบ")
    NumberService = int(input("ป้อนหมายเลขบริการ"))
    if NumberService == 1 :
        print("คุณต้องการถอนเงิน")
    elif NumberService == 2 :
        print("คุณต้องการโอนเงิน")
    elif NumberService == 3 :
        print("คุณต้องการเปิดบัญชีใหม่")
    else :
        print("หมายเลขบริการไม่ถูกต้อง")
else :
    print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")