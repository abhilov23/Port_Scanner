import socket #using sockets
from IPy import IP

def scan(target): #for taking multiple targets and scan them accoudingly
    converted_ip = check_ip(target)
    print('\n' + '[- scanning Target]' + str(target))
    for port in range(75, 82):
        port_scan(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip) #checking if it is a valid IP address
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip) #trying to figure out the ip address of the website


def port_scan(ipaddress, port):
    try:
        second_sock = socket.socket() #using a separate variable for the second socket object
        second_sock.settimeout(1)#setting up a timeout for fast scanning
        second_sock.connect((ipaddress, port))
        print('[+] Port '+ str(port) + ' is open')
    except:
        print('[!] Port ' + str(port) +  ' is closed')

targets = input('[+] Enter the target/s to scan: (split multiple targets with,):') #taking input from users
if ',' in targets: #if there is , in targets means use is specifying multiple targets otherwise not.
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)


