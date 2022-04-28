# Time limit
# n = int(input())
# n1, n2 = 0, 1
# for i in range(1, n):
#     if n == 0 or n == 1 or n == 2:
#         break
#     n3 = n1+n2
#     n1, n2 = n2, n3
#     if(i == n-1):
#         print(str(n3)[-1])
#         break
# if n == 0:
#     print(0)
# if n == 1 or n == 2:
#     print(1)

#########################################################
# Fastest One
n = int(input())


def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


print(str(_fib(n)[0])[-1])
