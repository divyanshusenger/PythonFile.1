
for i in range(1,6):
    k=i
    for j in range(1,6):
        if (j>=6-i):
            print(k, end=" ")
            k += 1
        else:
            print(" ",end=" ")
    print()
