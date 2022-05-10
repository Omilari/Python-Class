# two-dimensional lists

l1 = [[1, 2], [3, 4], [5, 6], [9, 2]]


for i in range(0, len(l1)):
    print(sum(l1[i]), end=" ")


list = [1, 2, 3, 4, 5]
for x in range(0, len(list) - 1):
    list[x] = list[x + 1]

print(list)
