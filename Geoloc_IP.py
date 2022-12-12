import requests

ip = requests.get('http://ipinfo.io')
ip_res = ip.json()
print(ip_res['loc'])

