import socket #using sockets
from IPy import IP

def check_ip(ip):
    try:
        IP(ip) #checking if it is a valid IP address
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip) #trying to figure out the ip address of the website

def get_banner(s): #taking the socket object inside this function so that we can grab the services of the same.
    return s.recv(2048) #receiving the socket data

def port_scan(ipaddress, port):
    try:
        second_sock = socket.socket() #using a separate variable for the second socket object
        second_sock.settimeout(3)#setting up a timeout for fast scanning
        second_sock.connect((ipaddress, port))
        try:
            banner = get_banner(second_sock) #grabbing a banner out of no where
            print('[+] Open Port '+ str(port) + ':' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port '+ str(port))
    except:
        pass #this will not print anything and just scan another function for the same.

def scan(target): #for taking multiple targets and scan them accoudingly
    converted_ip = check_ip(target)
    print('\n' + '[- scanning Target]' + str(target))
    for port in range(10, 90):
        port_scan(converted_ip, port)

targets = input('[+] Enter the target/s to scan: (split multiple targets with):') #taking input from users
if ',' in targets: #if there is , in targets means use is specifying multiple targets otherwise not.
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)