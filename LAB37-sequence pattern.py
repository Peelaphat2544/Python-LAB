#LAB37 Pattern Matching (Sequence pattern)
#List & tuple Apply

data = [1,2] #List

match data :
    case [] :
        print("ไม่มีข้อมูล")
    case [1,2] :
        print("มีข้อมูล 1,2")
    case [1,2,3] :
        print("มีข้อมูล 1,2,3")
    case _ :
        print("ไม่มีข้อมูลที่ต้องการ")



color = ("Red","Green","Blue") #Tuple

match color :
    case () :
        print("ไม่มีข้อมูล")
    case ("Red","Green") :
        print("มีข้อมูล แดง และ เขียว")
    case ("Red","Green","Blue") :
        print("มีข้อมูล สีแดง สีเขียว และ สีน้ำเงิน")
    case _ :
        print("ไม่มีข้อมูลที่ต้องการ")