import socket

def scanner():
    print("===== PORT SCANNER =====")

    ip_address=input("ENTER THE IP ADDRESS :\n")

    start=int(input("enter the start range :\n"))
    end=int(input("enter the end of the range :\n"))
    if start < 0 or end > 65535 or start > end:
        print("Invalid Port Range")
        return
    opened = 0 
    closed=0
    
    for i in range(start,end+1):
        scan = socket.socket( # we are having new socket per loop so that we can we start a new connection because the per socket is realated to that particular port and socket 
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        scan.settimeout(1)
        result=-1
        try:
            result=scan.connect_ex((ip_address,i))
        except socket.gaierror :
            print("IP address not valid")
            scan.close()
            return
        except OSError:
            print("OS ERROR")
            scan.close()
        if result==0:
            print(f"port : {i} is open")
            opened +=1
        else:
            print(f"port {i} is closed")
            closed+=1
        scan.close()
    for i in range(10):print("==",end=" ")
    print("Total Ports scanned : ",sum([opened,closed]))
    print(f"opened :{opened}\nclosed :{closed}")


scanner()
