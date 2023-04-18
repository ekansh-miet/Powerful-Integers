import math
n = int(input())
d = int(math.log10(n))
ans = n // 10**d + 9*d;
print(ans)