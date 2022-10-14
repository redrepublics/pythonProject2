# n = 10
# f = 0
# data = [i for i in reversed(range(f, n+1))]
# print(data)
#
# data_set = (n-1 + 0) / 2 * n
# data_real_number = (9 + 0) / 2 * 10
# print(data_set)
# print(data_real_number)

# Во сколько раз (примерно) возрастет время работы алгоритма сложностью
# O(n^2) по сравнению с O(n*log(n)) на входных данных размера n=10000?
# Ответ округлите до целого. Помните также, что логарифм берется по основанию 2.
# unit17.2.3
import math
n=10000
z = round(n / math.log(n, 2))
print(z)