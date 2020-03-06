def pn(n):
    d = 2
    while (n % d != 0):
        d += 1
    return d == n
a = input()
print(pn(int(a)))