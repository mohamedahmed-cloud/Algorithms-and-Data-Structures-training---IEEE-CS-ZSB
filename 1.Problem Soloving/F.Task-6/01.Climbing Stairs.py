def fib(n):
    if n<2: 
        return n
    n1=0
    n2=1
    n3=1
    for i in range(2,n+2):
        n3=n1+n2
        n1=n2
        n2=n3
    return n3
n=int(input())
print(fib(n))