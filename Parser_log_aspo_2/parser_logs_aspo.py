import glob
import os
import datetime
import configparser

ini_file = 'parser_logs_aspo.ini'
config = configparser.ConfigParser()
config.read(ini_file)
pars_type = 'xml'
os.chdir(os.getcwd())
now = datetime.datetime.now()
current_time_file = now.strftime("%y_%m_%d_%H_%M_%S")


def ini_pars():
    ini_list = list()
    ini_list.append(config["params"]["finding-errors"])
    return ini_list


def finding_errors():
    for file in glob.glob(f'*.{pars_type}'):
        with open(file, 'r') as result_file:
            for line in result_file:
                if ini_pars()[0] in line:
                    with open(f'{current_time_file}_error_report.txt', 'a+') as res:
                        res.write(line)


finding_errors()
