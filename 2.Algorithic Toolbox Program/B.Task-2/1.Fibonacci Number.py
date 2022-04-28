# Time Limiting
# n = int(input())


# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(n))
###############################################################################################################
# Good one passed all the test cases

# n = int(input())
# n1, n2 = 0, 1
# for i in range(1, n):
#     if n == 0 or n == 1 or n == 2:
#         break
#     n3 = n1+n2
#     n1, n2 = n2, n3
#     if(i == n-1):
#         print(n3)
#         break
# if n == 0:
#     print(0)
# elif n == 1 or n == 2:
#     print(1)

######################################################################################################
# Fastest one
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


print(_fib(n)[0])
