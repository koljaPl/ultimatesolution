m = int(input())
p = int(input())
n = int(input())
k = m * (p / 100)
for i in range(n):
    print(i + 1, m + k)
    k = k + k