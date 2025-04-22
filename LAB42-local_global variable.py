#LAB42 Variable [local & globle] 
balance = 10000 #global Variable
def displayBalance():
    print("ยอดเงินคงเหลือในบัญชี",balance,"บาท")

def deposit(value):
    global balance #global Variable กำหนดให้ฟังก์ชันมองเห็นเป็นตัวแปรสาธารณะ
    money = value #local Variable
    balance+=money
    print("ฝากเงิน",balance)

def withdraw(value):
    global balance
    money = value
    balance-=money #local Variable
    print("ถอนเงิน",balance)

displayBalance()
deposit(5000)
displayBalance()