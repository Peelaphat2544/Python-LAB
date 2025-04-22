#LAB34 Pattern Matching (Capture Pattern)

service = 0
match service:
    case 1 : 
        print("ฝากเงิน")
        print()
    case 2 : print("ถอนเงิน")
    case 3 : print("สอบถามยอเงินคงเหลือ")
    case service : print(f"หมายเลขบริการ {service} ไม่ถูกต้อง กรุณาทำรายการใหม่อีกครั้ง") #ถ้าไม่เข้า case ใด ๆ
    