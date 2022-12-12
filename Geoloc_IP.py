import requests


class IpRES:
    def __init__(self):
        self.ip = requests.get('http://ipinfo.io')
        self.ip_res = self.ip.json()

    def result_ip(self):
        print('IP: {0}\nГород: {1}\nСтрана: {3}\nКоординаты провайдера: {2}\nНаименование провайдера: {4}'
              .format((self.ip_res['ip']), (self.ip_res['city']), (self.ip_res['loc']), (self.ip_res['country']),
                      (self.ip_res['org'])))


pr = IpRES()
pr.result_ip()
