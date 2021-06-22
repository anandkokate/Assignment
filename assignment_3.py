def policeman_Thives(A,k):
    n=len(A)
    i=0
    l=0
    r=0
    count=0
    th=[]
    po=[]
    while i<n:
        if A[i]=='P':
            po.append(i)
        elif A[i]=='T':
            th.append(i)
        i+=1
    while l<len(th) and r<len(po):
        if(abs(th[l]-po[r])<=k):
            r+=1
            l+=1
            r+=1
        elif th[i]<po[r]:
            l+=1
        else:
            r+=1
    return r
    
            
    


T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    A=[]
    for _ in range(N):
        A.append(input().split())
    
print(policeman_Thives(A,K))
