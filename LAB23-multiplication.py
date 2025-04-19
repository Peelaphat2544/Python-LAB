#CHALLENG Mutiplication แม่สูตรคูณแบบกำหนดเป็นช่วง
start = int(input("กรุณากรอกแม่สูตรคูณเริ่มต้น"))
end = int(input("กรุณากรอกแม่สูตรคูณสิ้นสุด"))
for i in range(start,end+1):
    for j in range(1,13): # คูณด้วย 1-12
        if j == 1:
            print("สูตรคุณ แม่",i)
        print(f"{i}x{j}={i*j}")
        if j >= 12 :
            print("====================")