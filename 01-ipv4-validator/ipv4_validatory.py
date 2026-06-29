'''
PROJECT : IPv4 VALIDATOR
Validates IPv4 addresses accoding to standard IPv4 formatting rules

Author : VINIT KUMAR SINGH
'''
ip_address = input("enter the ip address ")
print(f"The IP address entered : {ip_address}")

def validator(ip_address):
    octects=ip_address.split(".")
    valid=True
    if len(octects) != 4 :  # to check if there are 4 octects only
        valid=False
    for num in octects :
      try:
          if num == '':  # to check if it has a blank octect
             valid=False
             break
          num=int(num) 
          if num > 255 or num < 0: # to check if it is in between 0 to 255
            valid=False
            break
      except ValueError :
         print("Entered value out of range")
         return False
       
    return valid

response =validator(ip_address)
if response is True :
   print("IP entered is valid")
else :
   print("Ip enterd is invalid")
