# He didn't give me the explanation or test cases
p, n = list(map(int, input().split()))


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
print(str(fib(n)[1]+fib(n)[0]-1)[p-1])
