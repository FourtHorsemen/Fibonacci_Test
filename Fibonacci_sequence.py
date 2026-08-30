n = 0
a = 0
b = 1

n = int(input("Enter value:"))

for i in range(n):
    print(a)
    a, b = b, a + b
