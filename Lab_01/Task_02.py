a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

print(type(a))
print(type(b))
print(type(c))

if a > b and a > c:
    print("A is greatest:", a)
elif b > a and b > c:
    print("B is greatest:", b)
elif c > a and c > b:
    print("C is greatest:", c)
else:
    print("There are at least two numbers that are equal and greatest.")
