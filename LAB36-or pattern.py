#Pattern Matching (OR pattern) ใช้เครื่องหมาย | แทน or

data = input("ป้อนคำนำหน้าชื่อของคุณ : ")

match data :
    case "เด็กชาย" | "นาย" :
        print("คุณเป็นเพศชาย")
    case "เด็กหญิง" | "นาง" | "นางสาว" :
        print("คุณเป็นเพศหญิง")
    case _ :
        print("ไม่พบข้อมูล")