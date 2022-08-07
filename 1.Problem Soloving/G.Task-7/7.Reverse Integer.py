def solve(x):
    # print(2**32)
    if x<2147483647+1 and x>-2147483412-1:
        if x>=0:
            s=str(x)
            s=s[::-1]
            if int(s)>2147483647+1 or int(s)<-2147483412:
                return 0
            return int(s)
        else:
            x=abs(x)
            s=str(x)
            s=s[::-1]
            if int(s)>2147483647+1 or int(s)<-2147483412:
                return 0
            return -int(s)
    return 0
import sys,math
x=int(sys.stdin.readline())
print(solve(x))