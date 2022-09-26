user_database = {'user':'password', 'iseedeadpeople': 'greedisgood','hesoyam': 'tgm'}
key = input("Введите логин\n")
value = input("Введите пароль\n")
def dict_user_data():
    if key in user_database.keys() and value in user_database.values():
        return True
    elif value not in user_database.values() or key not in user_database.keys():
        return False
    else:
        return False
fin_total = dict_user_data()
if fin_total != True:
     print("Вас нет в базе")
else:
     print("Вы в базе")




