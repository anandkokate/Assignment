def prime(n):
    li1=[]
    li2=[]
    for i in range (n+1,n+100):
        li1.append(i)
    for j in li1:
        prime_val = True
        for x in range(2,j-1):
            if j % x == 0:
                prime_val = False
                break
        if prime_val:
            li2.append(j)
    return min(li2)
n=int(input('Enter a number:'))
if n<=1:
    print('Prime number start from 2')
else:
    n1=prime(n)
    print(n1)
