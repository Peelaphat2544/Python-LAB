#LAB18 break & coninue
select = int(input("กรุณาเลือกการทำงาน 1 = break หรือ 2 = continue : "))

if select == 1:
    for i in range(0,10):
        if i == 5:
            break #เมื่อเจอคำสั่ง break ออกจากลูปทันทีและจบการทำงาน
        print(i)
    print("break ทำงานแล้ว")
elif select == 2:
    for i in range(0,10):
        if i == 5:
            print("continue ทำงานแล้ว")
            continue #เมื่อเจอคำสั่ง continue จะข้ามการทำงานจำนวนรอบนั้น
        print(i)
else:
    print("หมายเลขไม่ถูกต้อง")