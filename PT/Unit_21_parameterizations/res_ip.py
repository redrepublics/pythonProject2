from ping3 import ping


def t_test():
    if ping('ya.ruуууу'):
        print(True)
    else:
        print(False)

print(t_test())