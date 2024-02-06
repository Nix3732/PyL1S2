# # Задание 1
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b and a == c and b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# if a != b and a != c and b != c:
#     print(0)


# # Задание 2.1
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# Задание 2.2
n = int(input())
for i in range(1, n+1):
    print(' ' * (2*(n-i)+1), end=' ')
    for j in range(i, 0, -1):
        print(j, end=' ')
    for k in range(2, i+1):
        print(k, end=' ')
    print()