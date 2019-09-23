names=['alamin','dolar','fuad','sakiur']
courses =['python','java','c++']
student_details=[names,courses]
for s in student_details:
    for item in s:
        print(item,end=" ")
    print("\n")