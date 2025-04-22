#LAB33 Pattern Matching (Wildcard Pattern)

service = None
match service:
    case 1 : 
        print("ฝากเงิน")
        print()
    case 2 : print("ถอนเงิน")
    case 3 : print("สอบถามยอเงินคงเหลือ")
    case _ : print("หมายเลขบริการไม่ถูกต้อง") #ในกรณีที่ไม่ตรงกับ Case ใด ๆ ให้ทำคำสั่ง #default Case