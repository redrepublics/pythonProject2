import os

folder = os.getcwd()
root = folder
path = folder
files = os.listdir(path)
result = os.path.join(root, 'result.inf')  # Создать путь к окончательному текстовому файлу (result.txt)

with open(result, 'w', encoding='utf-8-sig') as r:
    for i in range(1, 30):
        print(i)
        fname = str(i) + '.txt'
        filename = os.path.join(path, fname)
        with open(filename, 'r', encoding='utf-8-sig') as f:
            for line in f:
                if '《' not in line:  # Пропустите строку, содержащую номер заголовка "
                    r.writelines(line)
            r.write('\n')


