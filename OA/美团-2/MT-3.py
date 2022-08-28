from decimal import Decimal
n, m = input().split()
n = int(n)
m = int(m)
temp = input("")
p = [int(n) for n in temp.split()]
temp = input("")
a = [int(n) for n in temp.split()]
diff = list()
base = 0
for i in range(n):
    base += p[i]/100*a[i]
    diff.append((100-p[i])/100*a[i])
diff.sort()
diff.reverse()
improve = sum(diff[0:m])
# print(round(base+improve, 2))
print(Decimal(base+improve).quantize(Decimal('0.00')))
