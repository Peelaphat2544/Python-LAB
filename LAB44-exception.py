#LAB44 Exception (การจัดการกับข้อผิดพลาดในโปรแกรม)
"""
มันแสดงใน Terminal
ArithmeticError #ข้อผิดพลาดเกี่ยวกับการคำนวณ
NameError #ข้อผิดพลาดเกี่ยวกับชื่อตัวแปร
TypeError #ข้อผิดพลาดเกี่ยวกับประเภทข้อมูล
ValueError #ข้อผิดพลาดเกี่ยวกับค่าข้อมูลไม่ตรงตามประเภทที่ระบุ
ZeroDivisionError: division by zero #ข้อผิดพลาดเกี่ยวกับการหารด้วย 0
"""
try:
    number1 = int(input("ป้อนตัวเลขที่ 1 : "))
    number2 = int(input("ป้อนตัวเลขที่ 2 : "))

    result = number1/number2
    print("ผลลัพธ์คือ : ",result)
except ValueError:
    print("ข้อมูลที่กรอกไม่ถูกต้อง ป้อนข้อมูลเฉพาะตัวเลข")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วย 0 ได้")    
finally:
    print("---------------------")
    print("จบโปรแกรม")