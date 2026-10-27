# n = int(input("Enter number of rows: "))

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()


n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()


row = int(input("Enter number of rows: "))

for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()



