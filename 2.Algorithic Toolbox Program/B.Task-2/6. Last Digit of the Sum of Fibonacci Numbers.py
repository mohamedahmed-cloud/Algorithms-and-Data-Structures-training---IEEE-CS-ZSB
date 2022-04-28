# # # Time limit

# n = int(input())
# if n > 2:
#     n1, n2 = 0, 1
#     sum1 = 1
#     for i in range(1, n):
#         if n == 0 or n == 1 or n == 2:
#             break
#         n3 = n1+n2
#         sum1 += n3
#         # print(sum1)
#         n1, n2 = n2, n3

#         if(i == n-1):
#             print(sum1)
#             print(str(sum1)[-1])
#             break

# # print(sum1)
# else:
#     if n == 0:
#         print(0)
#     elif n == 1:
#         print(1)
#     elif n == 2:
#         print(2)

#################################################################################

# faster one
n = int(input())


def fib(n):

    if n == 0:

        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:

            return (d, c + d)


# print(fib(n))
print(str(fib(n)[1]+fib(n)[0]-1)[-1])
