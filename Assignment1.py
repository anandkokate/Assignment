def adjacentduplicate(s1):
    li1=list(s1)
    s=None
    k=0
    for c in s1:
        if s!=c:
            li1[k]=c
            s=c
            k+=1
    return ''.join(li1[:k])
s1="AAABBBCCCAAA"
s1=adjacentduplicate(s1)
print(s1)



























