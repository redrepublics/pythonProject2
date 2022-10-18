import configparser

ini_files = "pars.ini"
config = configparser.ConfigParser()
config.read(ini_files)


def Depthini():
    depthini_id = list()
    depthini_id.append(config["params"]["Depth"])
    result = depthini_id[0]
    return int(result)


def GetIni():
    error_search_ini_id = list()
    error_search_ini_id.append(config["params"]["Params"])
    result = error_search_ini_id[0]
    return result
