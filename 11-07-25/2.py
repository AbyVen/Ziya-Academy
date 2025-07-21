rows = 5
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        if num % 3 == 0 and num % 5 == 0:
            break
        print(num, end=' ')
        num += 1
    else:
        num += 1  
        print()
        continue
    break