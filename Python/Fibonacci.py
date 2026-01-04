
n = int(input("Enter a number: "))

a = 0
b = 1

print(a)
print(b)

for i in range(n - 1):
    c = a + b
    print(c)
    a = b
    b = c
