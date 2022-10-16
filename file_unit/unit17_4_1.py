#рекурсия
# LIFO
def p(n):
    if n:
        p(n - 1)
        print(n)
    else:
        return

p(5)


G = {0 : [1, 2, 3],
     1 : [0, 2],
     2 : [0, 1],
     3 : [0]}
print(G)

