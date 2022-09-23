def adder(*nums):
    sum_ = 10
    for n in nums:
        sum_ *= n

    return sum_


print(adder())  # 0
print(adder(1))  # 1
print(adder(1, 2))  # 3
print(adder(1, 2, 3))  # 6