my_file = open(r'E:\python_read_file.txt','rt', encoding="utf-8")
for line in my_file:
    print(line)
my_file.close()
# print(my_file.readlines())

# my_file = open('E:\python_test1.txt','w', encoding="utf-8")
# my_file.write('тестовый тест')
# print('!!!!!!!!!!!', file=my_file)
#
# my_file.close('E:\python_test1.txt')