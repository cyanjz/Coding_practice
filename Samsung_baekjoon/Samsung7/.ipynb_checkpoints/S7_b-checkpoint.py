n,*a=map(int,open(r:=0).read().split())
d=[0]*30
for s in range(n):t,p=a[2*s:2*s+2];d[s+t]=max(d[s+t],r+p);r=max(r,d[s+1])
print(r)