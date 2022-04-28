########################################
#  Very Slow
# First One
# a, b = list(map(int, input().split()))
# a1 = 0


# def GCD(a, b):
#     if b == 0:
#         return b
#     else:
#         b = a % b
#     return(b)
# print(GCD(a, b))
#################################################################

# Second One
# Time limit
# we her will depend on the first number is small than second

# n, p = list(map(int, input().split()))
# # n = min(n, p)
# # p = max(n, p)
# i = 1
# out = 0
# while n > 1:
#     if n % 2 == 0:
#         GCD = n/i
#         if p % GCD == 0:
#             print(int(GCD))
#             out = 1
#             break
#     else:
#         GCD = n/i
#         if p % GCD == 0:
#             print(int(GCD))
#             out = 1
#             break
#     i += 1
#     n -= 1
# if out == 0:
#     print(1)

# Thrid Solution
a, b = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


print(gcd(a, b))
