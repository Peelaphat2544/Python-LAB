#Match Statement (คล้าย Switchcase ในภาษา C)
'''
match X:
    case Value1 :
        คำสั่ง
'''

NumberService = (input("กรุณาป้อนหมายเลขบริการ : "))

match NumberService:
    case "1" :
        print("คุณเลือกหมายเลข 1",NumberService,"ฝากเงิน")
    case "2":
        print("คุณเลือกหมายเลข 2",NumberService,"ถอนเงิน" )
    case "3":
        print("คุณเลือกหมายเลข 3",NumberService,"โอนเงิน")
    case "":
        print("คุณไม่ได้เลือกหมายเลข",NumberService,"หมายเลขบริการไม่ถูกต้อง")

