#LAB35 Pattern Matching (Guard)

# 100 = คะแนนสอบได้เต็ม 50-99 = ผ่านเกณฑ์การสอบวัดผล

score = int(input("กรุณากรอกคะแนนสอบของคุณ (0-100) : "))
print("คะแนนของคุณ คือ ", score)

match score:
    case 100:
        print("คุณได้คะแนนเต็ม")
    case score if score >= 50 and score < 100:
        print("สอบผ่านเกณฑ์")
    case _:
        print("สอบไม่ผ่านเกณฑ์")
