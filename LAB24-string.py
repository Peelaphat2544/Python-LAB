#LAB24 String (การจัดการกับข้อความ)
"""
"""
name = "Peelaphat"
lastname = "Kaewkong"
X = name+lastname


address = """
xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxx
"""

#P-e-e-l-p-h-a-t- -K-e-a-w-k-o-n-g
#0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16
#[--16--15--14--13--12--11--10--9--8--9--7--6--5--4--3--2--1

print(X[0]) #index
print(X[0:]) #index
print(X[0:9]) #index
print(X[0:9:2]) #index
print(X[-1])
print(X[-8])
print(X[:9])
print(len(address)) #lines และตรวจสอบตัวอักษร โดยใช้คำสั่ง len()

for c in X :
    print(c)


dd = 12
month = "มกราคม"
year = 2544

print(f"คุณเกิดวันที่{dd} เดือน {month} พ.ศ. {year}") #F-String

dd = 12
month = {"มกราคม"}
year = 2544
massage = f"คุณเกิดวันที่ {dd} เดือน {month} ปี พ.ศ. {year}"
print(massage) #F-String

Money = 200
print(f"คุณมีเงิน : {Money:.2f}")

Dept = f"คุณมีหนี้จังเสีย : {200000000000000000:.5f} บาท"
print(Dept)

Net_Value = 100000.988358
print(f"เอาทศนิยม 1 ตำแหน่ง : {Net_Value:.1f} บาท")
print(f"เอาทศนิยม 2 ตำแหน่ง : {Net_Value:.2f} บาท")
print(f"เอาทศนิยม 3 ตำแหน่ง : {Net_Value:.3f} บาท")
print(f"เอาทศนิยม 4 ตำแหน่ง : {Net_Value:.4f} บาท")
print(f"เอาทศนิยม 5 ตำแหน่ง : {Net_Value:.5f} บาท")



