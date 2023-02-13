import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print("\n Scanning target/s: "+str(target))
    for port in range(1,100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(sck):
    return sck.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        try:
            banner = get_banner(sock)
            print("[+] Open Port:- "+str(port)+" : "+str(banner))
        except:
            print("[+] Open Port:- "+str(port))
    except:
        pass


targets = input("[+] Enter Target/s to scan(if multiple targets separate them with comma):- ")
if ',' in targets:
    for ip_address in targets.split(','):
        scan(ip_address.strip(' '))
else:
    scan(targets)


