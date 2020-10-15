def fact(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
       print(a)
       print(b)
       for j in range(2,n):
             j=a+b
             a=b
             b=j
             print(j)
res=fact(4)
