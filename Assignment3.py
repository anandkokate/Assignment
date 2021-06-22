for _ in range(int(input())):
    x,y=map(int,input().split())
count=0
if(x>y):
    for j in range(x):
        l=list(map(str,input().split()))
        c=0
        for i in range(x-y):
            l1=l[i:i+y+1]
            k=1
            while k!=0:
                if("P" in l1 and "T" in l1):
                    l[i+l1.index("P")]=c
                    l[i+l1.index("T")]=c
                    l1[l1.index("P")]=c
                    l1[l1.index("T")]=c
                    c+=1
                else:
                    k=0
        count+=c
    print(count)
        
else:
    for j in range(x):
        d=list(map(str,input().split()))
        l={"P":0,"T":0}
        c=0
        for i in d:
            l[i]+=1
        if(l["P"]>l["T"]):
            c+=l["T"]
        else:
            c+=l["P"]

        count+=c
    print(count)

