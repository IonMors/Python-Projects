import socket # module for low-level networkting functionality 
              # allowing to communicate over the internet using various network protocols, such as TCP and UDP
from IPy import IP # IP address manipulation    

def scan(target):
    converted_ip = check_ip(target) # takes a target IP address or domain name as input, converts it to an IP address (if necessary)
    print("\n Scanning target/s: "+str(target))
    for port in range(1,100):
        scan_port(converted_ip, port) # scans for open_ports

def check_ip(ip):
    try:
        IP(ip) # checks if the input is a valid IP address or domain name, and returns the IP address if the input is a domain name
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

# A banner is a message or string of text that is sent by a server or application when a connection is established with a client. 
# The banner typically contains information about the server or application, such as its name, version number, and other details.
def get_banner(sck):
    return sck.recv(1024)

def scan_port(ipaddress, port): # creates a socket
    try:
        sock = socket.socket() # function is used to create a new socket object that can be used to establish a connection with another program or device over a network.
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


