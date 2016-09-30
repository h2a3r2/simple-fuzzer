import socket, sys
print "############################################"
print "#        Welcome to Simple Fuzzer          #\r"
print "#                                          #\r"
print "#version-beta          by-h2a3r2@gmail.com #"
print "############################################\r\n"
def ftp(username, password, command):
    print ("\r\n")
    host = raw_input ('Enter the Target IP Address:')
    port = raw_input ('Enter the Port to connect to the Target:')
    port = int(port)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.recv(1024)
            print "\r\n            connection established\r\n"
            minimum = raw_input ('Enter Minimum buffer length:')
            minimum = int(minimum)
            maximum = raw_input ('Enter Maximum buffer length:')
            maximum = int(maximum)
            break
        except:
            print "Unable to connect to the host"
            sys.exit()
    if (username == "1"):
        while (minimum < maximum):
            try:
                s.send("USER " + "A" * minimum +"\r\n")
                print "Length Sent: " + str(minimum)
                minimum += 10
            except:
                print " crashed at:" + str(minimum)
                sys.exit()
    if (password == "1"):
        user = raw_input('Enter the user name:')
        print ("Fuzzing started on Password command...")
        while (minimum < maximum):
            try:
                s.send("USER "+user)
                s.recv(1024)
                s.send("PASS " + "A" * minimum + "\r\n")
                print "Length Sent: " + str(minimum)
                minimum += 10
            except:
                print " crashed at:" + str(minimum)
                sys.exit()
    if (command == "1"):
        print ("\r\n                   NOTE: Valid Username and Password is required to perform this Attack\r\n")
        user = raw_input('Enter the user name:')
        passwd = raw_input('Enter the Password for ' + user +":")
        s.send("USER "+user)
        response=s.recv(1024)
        s.send("PASS " + passwd)
        response=s.recv(1024)
        if "230" in response:
            print "\r\n            Authentication Success\r\n"
            cmd = raw_input (str('Enter the command in CAPS to start the fuzz \r\nPASV\r\nLIST\r\nCWD\r\nMKD\r\nRMD\r\nGET\r\nPUT\r\nENTER to Attack:'))
            if (cmd ==("PASV" or "LIST" or "CWD" or "MKD" or "GET" or "PUT")):
                while (minimum < maximum):
                    try:
                        s.send(cmd + " " + "A" * minimum + "\r\n")
                        print "Length Sent: " + str(minimum)
                        minimum += 10
                    except:
                        print " crashed at:" + str(minimum)
                        sys.exit()
            else:
                print("Entered command is not valid.. try Again")
                sys.exit()
        else:
            print "Authentication falied"
            sys.exit()
def custom(command):
    print ("\r\n")
    host = raw_input ('Enter the Target IP Address:')
    port = raw_input ('Enter the Port to connect to the Target:')
    port = int(port)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.recv(1024)
            print "\r\n            connection established\r\n"
            print "\r\n     Note: KNOWN Command is required to perform this attack. connect #nc target port  and type HELP to get list of commands\r\n"  
            minimum = raw_input ('Enter Minimum buffer length:')
            minimum = int(minimum)
            maximum = raw_input ('Enter Maximum buffer length:')
            maximum = int(maximum)
            break
        except:
            print "Unable to connect to the host"
            sys.exit()
    if (command == "0"):
        cmd = raw_input ('Enter the command to start the Attack:')
        while (minimum < maximum):
            try:
                s.send(cmd + " " + "A" * minimum + "\r\n")
                s.recv(1024)
                print "Length Sent: " + str(minimum)
                minimum += 10
            except:
                print " crashed at:" + str(minimum)
                sys.exit()
    if (command == "1"):
        while (minimum < maximum):
            try:
                s.send("A" * minimum)
                print "Length Sent: " + str(minimum)
                minimum += 10
            except:
                print " crashed at:" + str(minimum)
                sys.exit()
            
#print ("\r\n")
print "1: Start Fuzzing FTP\r\n"
print "2: Start Fuzzing Custom Application\r\n"
print "3: Payload generator\r\n"
print "4: Generate Payload with specific File Extension\r\n"
c = raw_input ('Enter your option:')
c = int(c)
if (c == 1):
    print "\r\n"
    print "1: Fuzz in User Command \r\n"
    print "2: Fuzz in Password Command \r\n"
    print "3: POST Authentication Fuzz in KNOWN Command \r\n"
    option = raw_input ('Enter the option the Start the Fuzz:')
    option = int(option)
    if (option == 1):
        ftp("1", "0", "0")
        print "increse the maximum buffer length and try again "
    if (option == 2):
        ftp("0", "1", "0")
        print "increse the maximum buffer length and try again "
    if (option == 3):
        ftp("0", "0", "1")
        print "increse the maximum buffer length and try again "
elif (c == 2):
    print "\r\n"
    print "1: Fuzz using KNOWN Command \r\n"
    print "2: Fuzz with RAW Input \r\n"
    cus = raw_input ('Enter the option the Start the Fuzz:')
    cus = int(cus)
    if (cus == 1):
        custom("0")
        print "increse the maximum buffer length and try again "
    if (cus == 2):
        custom("1")
        print "increse the maximum buffer length and try again "
elif (c ==3):
    print "\r\n"
    payload = raw_input ('Enter the maximum size to generate the payload:')
    payload =int(payload)
    print("A"*payload)
    sys.exit()
elif (c == 4):
    print "\r\n"
    size = raw_input ('Enter the maximum size to generate the payload:')
    size =int(size)
    s=size * "A"
    print("creating new  file")
    name=raw_input ("enter the name of file:")
    extension=raw_input ("enter extension of file without '.':")
    try:
        name=name+"."+extension
        file=open(name,'a')
        file.write(s)
        file.close()
        print"Payload was successfully created"
    except:
        print("error occured")
        sys.exit()
else:
    print "Invalid Option.. try again"
