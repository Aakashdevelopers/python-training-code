# n = int(input("Enter number of rows: "))

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()


# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")

#     for k in range(2 * i - 1):
#         print("*", end="")

#     print()


# row = int(input("Enter number of rows: "))

# for i in range(1, row + 1):
#     for j in range(row - i):
#         print(" ", end="")

#     for k in range(2 * i - 1):
#         print("1", end="")

#     print()

# number = [2,5,5,7,]

# even = 0
# odd = 0

# for num in number:
#     if num%2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even Number ",even)
# print("Odd Number",odd)


# numbers = [1, 2, 2, 3, 1, 2, 4, 3]

# # method 1
# for num in numbers:
#     print(num, "appears", numbers.count(num))



# # method2

# for num in numbers:
#     count = 0
#     for item in numbers:
#      if item == num:
#         count +=1
# print(num, "Appears", count, "times")


# numbers = [1, 2, 2, 3, 1, 2, 4, 3]
# visited = []

# for num in numbers:
#     if num not in visited:
#         count = 0

#         for item in numbers:
#             if item == num:
#                 count += 1

#         print(num, "appears", count, "times")
#         visited.append(num)


numbers = [1, 2, 2, 3, 1, 2, 4, 3]

most_frequent = numbers[0]
max_count = 0

for num in numbers:
    count = numbers.count(num)

    if count> max_count:
        max_count = count 
        most_frequent = num

print("most frequent element", most_frequent)
print("Frequency",max_count)