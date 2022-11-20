def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@do_twice
def t_twice(str):
    print("Этот вызов возвращает строку {0}".format(str))
    return "Done"

decorated_value = t_twice("single")
print(decorated_value)
print(t_twice.__name__)