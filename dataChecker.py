import re
def isaccountNo(accountNo):
    try:
        b=int(accountNo)
    except:return False
    if len(accountNo)!=10:
        return False
    else:return True

def isAmount(amount):
    try:
        if type(int(amount))==int:
           return True
    except: return False

def isName(name):
    return all(char.isalpha() or char.isspace() for char in name)

def isAge(age):
    return all(char.isdigit() for char in str(age)) and len(str(age))>=2 and len(str(age))<=3

def isAddress(address):
    return all(char.isalpha() for char in address)

def isMobile(mob):
    mob=str(mob)
    if len(mob)!=10: return False
    return all(char.isdigit() for char in mob)

def isAadhar(aadhar):
    aadhar=str(aadhar)
    if len(aadhar)!=12: return False
    return all(char.isdigit() for char in aadhar)

def isEmail(mail):
    pattern=r'.*@gmail.com'
    if re.search(pattern,mail)==None: return False
    return True