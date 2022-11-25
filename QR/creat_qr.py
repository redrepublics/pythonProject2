import qrcode

"""Простая генерация QR-кода
Выдает по переменной, можно реализовать ввод с консоли любой str параметр"""


def qr_cr(format_date, name_user):
    result_img = f'{name_user}qr_result.png'
    data_site = format_date
    img = qrcode.make(data_site)
    img.save(result_img)
    return img.show(result_img)


qr_cr('https://github.com/redrepublics', 'Владислав Жеребьев ')
