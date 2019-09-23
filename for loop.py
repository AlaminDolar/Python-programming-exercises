
i = 1
while i<=100:
    if i%2==0:
          print(i,end='\t')
    i = i+1


num = int(input('Enter any Number: '))
i =1
while i<=10:
    print(num, 'X', i, '=', (num*i))
    i =i+1
    
    
    
num = int(input("enter the factorial: "))
n=num
fact =1
while num>0:
    fact=fact*num
    num=num-1
print("factorial of",n,"is: ",fact)