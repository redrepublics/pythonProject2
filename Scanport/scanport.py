import socket
import datetime


def scan_port(ip_add, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    now = datetime.datetime.now()
    current_time = now.strftime("%Y %b %d %A %H:%M:%S ")
    try:
        with open('report.txt', 'a+') as file:
            connect = sock.connect((ip_add, port))
            print(current_time, ('-'*10), 'IP :', ip_add, 'Port :', port, ' its open', 'Protocol :',
                  ports[port], ('-'*10))
            file.write('{0} IP: {1}, Port: {2}, Protocol: {3}\n'.format(current_time, ip_add, port, ports[port]))
            sock.close()
    except:
        print(current_time, 'its block', port, ports[port])
        pass


ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
    115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
    179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
    514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
    995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
    3268: "LDAP", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin"}

ip_add = input('Введите IP хоста для сканирования: ')
# '192.168.31.250'
if ip_add:
    for i in ports:
        scan_port(ip_add, i)
else:
    ip_add = 'localhost'
    for i in ports:
        scan_port(ip_add, i)
