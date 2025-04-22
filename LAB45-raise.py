#LAB45 Raise (การจัดการข้อผิดพลาดโดยการกำหนดเอง)

try:
    number1 = int(input("ป้อนตัวเลขที่ 1 : "))
    number2 = int(input("ป้อนตัวเลขที่ 2 : "))
    if number1 < 0 or number2 < 0:
        raise Exception("ข้อมูลตัวเลขต้องเป็นค่าบวกเท่านั้น") #เพิ่มการจัดการข้อผิดพลาดด้วยตนเอง
    result = number1/number2
    print("ผลลัพธ์คือ : ",result)
except ValueError:
    print("ข้อมูลที่กรอกไม่ถูกต้อง ป้อนข้อมูลเฉพาะตัวเลข")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วย 0 ได้")    
finally:
    print("---------------------")
    print("จบโปรแกรม")
    