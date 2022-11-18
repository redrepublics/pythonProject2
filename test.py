def func(func2):

    def func3(*args, **kwargs):
        print(f'Я вижу тебя внутри {func2.__name__}')
        print(f'Вот твои args: {args}')
        print(f'А вот твои kwargs:  {kwargs}')
        func2(*args, **kwargs)
    return func3


@func
def t_func(a, b, c, d='Я kwarg тут живу определи меня'):
    return a, b, c, d


t_func(1, 2, 3, d='А я томат')