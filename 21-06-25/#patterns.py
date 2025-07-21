#patterns
#(a)
for i in range(1,6):
     print(str(i) * i)

#(b)
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#(c)
num = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

