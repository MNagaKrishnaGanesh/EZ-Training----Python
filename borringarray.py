n=int(input("enter :"))
l=list(map(int,input("enter:").split( )))
l.sort()
i,j=0,len(l)-1
res=0
while i<j:
    res+=abs(l[i]-l[j])
    i+=1
    j-=1
print(res)