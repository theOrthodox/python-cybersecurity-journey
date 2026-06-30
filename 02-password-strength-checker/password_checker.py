print("===== WELCOME TO PASSWORD STRENGTH CHECKER =====")
password=input("Please enter your password \t")

def password_checker(password):
    has_length = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    specl = ['!', '@', '#', '$', '%','^', '&', '*', '(' ,')', '_' ,'+', '-', '=', '?' ,'/', '.']

    if len(password) >= 8 :
        has_length = True

    for word in password :
        if word.isupper():
            has_upper = True
        if word.islower():
            has_lower = True
        if word.isdigit():
            has_digit = True
        if word in specl:
            has_special = True

    if has_digit and has_length and has_lower and has_special and has_upper :
        return True
    else :
        return False

print(f"the password entered is : {password}")
if password_checker(password):
    print("strong")
else:
    print("Weak") 
