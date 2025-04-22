#LAB32 Pattern Matching (Literal Pattern)

service = None
match service:
    case 1 : 
        print("ฝากเงิน")
        print()
    case 2 : print("ถอนเงิน")
    case 3 : print("สอบถามยอเงินคงเหลือ")
    case None : print("ข้อมูลไม่ถูกต้อง")