import configparser

ini_files = "pars.ini"
config = configparser.ConfigParser()
config.read(ini_files)


def dept_ini():
    dept_ini_id = list()
    dept_ini_id.append(config["params"]["Depth"])
    result = dept_ini_id[0]
    return int(result)


def params_ini():
    error_search_ini_id = list()
    error_search_ini_id.append(config["params"]["Params"])
    result = error_search_ini_id[0]
    return result
