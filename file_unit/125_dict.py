# Напишите программу, которая получает на вход
# название книги, фамилию автора и год выпуска.
# Полученные данные должны быть преобразованы в словарь
# и в таком представлении выведены в консоль.



name_book = input("Название книги ")
fio = input("Фамилия автора ")
year = input ("Год издания ")
lib_disct = {'name_book': name_book, 'fio':fio , 'year':year }
print (lib_disct)