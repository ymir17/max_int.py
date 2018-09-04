n = int(input("Enter the length of the sequence: ")) # Do not change this line
a = 1
b = 2
c = 3

print(a)
print(b)
print(c)
for i in range(0, n-3):
    d = a + b + c

    a = b
    b = c
    c = d
    print(d)