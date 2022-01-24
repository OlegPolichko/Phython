for a in range (1, 11):
    for b in range (1, 11):
        print(a, "x", b, "=", a*b)
        


print("k!=1 * 2 * 3 * ... * k")
k=int(input("Введите k "))
a=1
for b in range(1, k+1):
    a*=b
print(a)