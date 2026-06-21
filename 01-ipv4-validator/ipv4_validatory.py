'''
PROJECT : IPv4 VALIDATOR
Validates IPv4 addresses accoding to standard IPv4 formatting rules

Authon : VINIT KUMAR SINGH
'''
ip_address = input("enter the ip address ")
print(f"The IP address entered : {ip_address}")

def validator(ip_address):
    octects = list()
    octects=ip_address.split(".")
    valid=True
    if len(octects) != 4 :
        valid=False
    for num in octects :
      try:
          num=int(num) 
          if num > 255 or num < 0:
            valid=False
            break
      except :
         valid=False
       
    if valid == True :
       return True
    else :
      return False
      
response =validator(ip_address)
if response is True :
   print("IP entered is valid")
else :
   print("Ip enterd is invalid")
