def analyzer():
    file=input("Enter the file path\n")
    try:
        with open(file) as logs:
         log_seg=logs.readlines()
    except FileNotFoundError:
        print("File not Found")
        return
    
    checks = {
    "Failed_login" :0,
    "Password_reset" :0,
    "Account_lockout" :0,
    "Suspicious_activity" :0
    }

    ip_address=list()
    
    for events in log_seg:
        if "Failed login" in events:
            checks["Failed_login"]+=1
        if "Password reset" in events:
           checks["Password_reset"]+=1
        if "Suspicious activity" in events:
            checks["Suspicious_activity"]+=1
        if "Account locked" in events:
            checks["Account_lockout"]+=1
        event=events.split()
        if "from" in event:
            if event[-1] in ip_address:
                continue
            else:
                ip_address.append(event[-1])

    
    print("===== SECURITY EVENT REPORT ===== \n")
    print(f"Failed Login Attempts : {checks.get('Failed_login')}")
    print(f"Password Resets : {checks.get('Password_reset')}")
    print(f"Suspicious Activity : {checks.get('Suspicious_activity')}")
    print(f"Account Lockout : {checks.get('Account_lockout')}\n")

    threat_level = sum(checks.values())
    print(f"Total Security Events : {threat_level}")
    if threat_level<=2:
        print("Threat Level : LOW \n")
    elif threat_level>2 and threat_level<=5:
        print("Threat Level : MEDIUM \n")
    else:
        print("Threat Level : HIGH \n")
    
    maximum=max(checks.values())
    if maximum==checks.get("Failed_login"):
        print(f"Most Frequent Event   : Failed Login")
    if maximum==checks.get("Password_reset"):
        print(f"Most Frequent Event   : Password Reset")
    if maximum==checks.get("Suspicious_activity"):
        print(f"Most Frequent Event   : Suspicious Activity")
    if maximum==checks.get("Account_lockout"):
        print(f"Most Frequent Event   : Account Lockout")
    
    print("="*30)

    print("===== IOCs FOUND =====")
    for ip in ip_address:
        print(f"->\t{ip}\n")
    print("Unique IP Found ",len(ip_address))

analyzer()

