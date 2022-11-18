
def most_frequent(input_list):
    counter = 0
    num = input_list[0]

    for i in input_list:
        curr_frequency = input_list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


result = input("Введити слова через пробел, по окончанию нажмите Enter: ").split()
print(most_frequent(result))
