#Challenge multiplication (สูตรคูณ)

'''
สร้างแม่สูตรคูณ
2x1=2
2x2=4
2x3=6
2x4=8
2x5=10
2x6=12
2x7=14
2x8=16
2x9=18
2x10=20
2x11=22
2x12=24
'''
number = int(input("ป้อนตัวเลขแม่สูตรคูณ"))

for i in range(1,13):
    print(f"{number}x{i}={number*i}")