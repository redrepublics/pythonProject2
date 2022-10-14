import configparser

def GetIni():
    ini_files = "pars.ini"
    config = configparser.ConfigParser()
    config.read(ini_files)
    error_search_ini_id = list()
    error_search_ini_id.append(config["params"]["Params"])
    result = error_search_ini_id[0]
    return result

