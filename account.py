import mysql.connector
#import hashlib
import random

db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
def createNewAccount(userName,age,address,aadharNo,email,password,mobileNo):
    db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
    #password1=hashlib.sha256(password.encode()).hexdigest()
    accountNo=random.randrange(4000000000,6000000000)
    accountNo=str(accountNo)
    cursor=db.cursor()
    age=int(age)
    cursor.execute("INSERT INTO user(account_no,u_name,age,address,aadhar_no,email,u_password,mobile) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(accountNo,userName,age,address,aadharNo,email,password,mobileNo))
    cursor.execute("INSERT INTO BALANCE(account_no,balance) VALUES(%s,%s)",(accountNo,0))
    db.commit()
    db.close()
    return accountNo

def login1(account,password):
    db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
    cursor=db.cursor()
    cursor.execute("select u_password from user where account_no=%s"%account)
    realPass=cursor.fetchone()
    db.close()
    #password=hashlib.sha256(password.encode()).hexdigest()
    if realPass[0]==password:
        return True
    else:return False

def deposit(account,amount):
    db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
    cursor=db.cursor()
    cursor.execute("UPDATE balance SET balance=balance+%s WHERE account_no=%s",(int(amount),account))
    db.commit()
    db.close()

def Withdraw(account,amount):
    db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
    cursor=db.cursor()
    cursor.execute("SELECT balance from balance where account_no=%s"%account)
    balance=cursor.fetchone()[0]
    if balance>=int(amount):
        cursor.execute("UPDATE balance SET balance=balance-%s WHERE account_no=%s",(int(amount),account))
        db.commit()
        db.close()
        return True
    else:return False
    
def checkBal(account):
    db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
    cursor=db.cursor()
    cursor.execute("SELECT balance from balance WHERE account_no=%s"%account)
    return cursor.fetchone()[0]

def changepassword(account,password,newpassword):
    db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
    cursor=db.cursor()
    try:
        cursor.execute("UPDATE user set u_password=%s where account_no=%s",(newpassword,account))
        db.commit()
        db.close()
        return True
    except:
        return False
    
def deleteAcc(account):
    balance=-1
    db=mysql.connector.connect(host='localhost',user='root',password='preet2005***',database='bank',auth_plugin='mysql_native_password')
    cursor=db.cursor()
    cursor.execute("SELECT balance from balance where account_no='%s'"%account)
    balance=cursor.fetchone()[0]
    cursor.execute("DELETE FROM user WHERE account_no='%s'"%account)
    cursor.execute("DELETE FROM balance WHERE account_no='%s'"%account)
    db.commit()
    db.close()
    return int(balance)