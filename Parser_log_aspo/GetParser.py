import os

folder = os.getcwd()
init_list = ['.xml', '.txt', 'test.xml', 'pars_result']
format_start = init_list[0]
format_finish = init_list[1]
test_xml = init_list[2]
my_dir = init_list[3]


def dir_cr():
    check_folder = os.path.isdir(my_dir)
    if not check_folder:
        os.makedirs(my_dir)
        return print("Создана папка : ", my_dir, flush=True)


# переводим xml в txt
def folder_dir():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename):
            continue
        else:
            os.path.splitext(filename)
            newname = infilename.replace(format_start, format_finish)
            os.rename(infilename, newname)


# переводим txt в xml
def folder_dir_return():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename):
            continue
        else:
            os.path.splitext(filename)
            newname = infilename.replace(format_finish, format_start)
            os.rename(infilename, newname)
