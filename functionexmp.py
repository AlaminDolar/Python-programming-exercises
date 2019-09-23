def total_marks(m1,m2,m3):
    total = m1+m2+m3
    return total


def avarage(total):
    avg= total/3
    return avg

def grade(avg):
    if avg>80:
        print("A")
    elif avg>60:
        print("B")
    elif avg>40:
        print("C")
    else:
        print("fail")
        
total = total_marks(80,90,71)
avg = avarage(total)
print("Your total marks: {}\navarage : {} ".format(total,avg))

grade(avg)
