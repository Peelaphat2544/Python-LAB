#LAB43 Return keyword

balance = 10000 #global Variable
def displayBalance():
    print("ยอดเงินคงเหลือในบัญชี",balance,"บาท")

def deposit(value):
    global balance #global Variable กำหนดให้ฟังก์ชันมองเห็นเป็นตัวแปรสาธารณะ
    money = value #local Variable
    if(money < 0):
        print("ฝากไม่สำเร็จ")
        return #กระโดดออกจากฟังก์ชัน บรรทัดถัดไปจะไม่ทำงาน
    balance+=money
    print("ฝากเงิน",balance)

def withdraw(value):
    global balance
    money = value
    if(money < 0 or balance < money):
        print("ถอนไม่สำเร็จ")
        return #กระโดดออกจากฟังก์ชัน บรรทัดถัดไปจะไม่ทำงาน
    balance-=money #local Variable
    print("ถอนเงิน",balance)

displayBalance()
deposit(10000)
displayBalance()
withdraw(600)
displayBalance()