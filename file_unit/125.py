#1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#1 1 2 3 5 8 13 21 34 55

L = list(map(float, input().split()))
L[0], L[-1] = L[-1], L[0]
L.append(sum(L))
print(L)

