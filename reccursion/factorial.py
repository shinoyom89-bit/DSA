def fact(n):
    if n==1:
        return n
    elif n==0:
        return 0
    return n*fact(n-1)
res=fact(5)
print(res)