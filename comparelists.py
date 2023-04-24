
L1 = [[1, 1, 2], [2, 3, 5], [3, 2, 8]]
L2 = [[2, 1, 6], [3, 2, 8], [1, 3, 5], [4, 4, 7]]

for i in range(max(len(L1), len(L2))):
    a = getitem(L1, i, [])
    b = getitem(L2, i, [])
    diff = []

for j in range(max(len(a), len(b))):
    if not getitem(a, j) == getitem(b, j):
        diff.append(j)

print (diff)
