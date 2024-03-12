from math import factorial
h =[]
n = 5
f = factorial(5)
# h.append({n: f})

for i in range(1, n):
    h.append({i: factorial(i)})

print(h[-2:])

