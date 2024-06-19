'''n=int(input("enter the n values "))
l=list(map(int,input("enter the give array").split()))
pos=0
res=0
for i in l:
    pos+=i
    if pos==0:
        res+=1
print(res)'''
str=input()
count=0
for i in str:
    if " " in i:
        count+=1
print(f"counting of space in the string {count}")
    