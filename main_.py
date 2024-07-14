from tkinter import *
from account import *
import tkinter.messagebox as messagebox
mainWindow=Tk()
mainWindow.geometry("500x480")
mainWindow.title("ABC BANK")
mainWindow.config(background='#E7F0DC')
image=PhotoImage(file="abcbank 1.png")
#mainWindow.iconphoto(False,image)
label1=Label(mainWindow,image=image,padx=30,pady=30)
#label1.grid(row="0",column="2")
label1.pack()
frame=Frame(mainWindow,padx=10,pady=10)
frame.pack()
accountLabel=Label(frame, text="Enter account no:")
#accountLabel.place(x=20,y=15,width=25)
accountLabel.grid(row="1",column="1")

accountNo = Entry(frame)
#accountNo.place(x=20,y=15,width=25)
accountNo.grid(row="1",column="2")

passLabel=Label(frame, text="Enter password :")
#passLabel.place(x=20,y=35,width=25)
passLabel.grid(row="2",column="1")

Password = Entry(frame,show='*')
#Password.place(x=20,y=35,width=25)
Password.grid(row="2",column="2")
frame2=Frame(mainWindow,padx=10,pady=10)
frame2.pack()
def login():
        passwordB=Password.get()
        AccountNo=accountNo.get()
        if login1(AccountNo,passwordB):
             messagebox.showinfo("succesfully logged in","login successfull!")
             menu()
        else: messagebox.showerror("Login Failed", "Invalid account number or password")

loginB=Button(frame2,text="Login",command=login)
loginB.grid(row="0",column="0")
#loginB.pack()
def menu():
      menuwin=Tk()
      menuwin.geometry("720x720")
      menuwin.title("Services-ABC BANK")
      label=Label(menuwin,text="services:",font=("arial",18)).pack()
      def depo():
          depositwin=Toplevel()
          accountnoLbel=Label(depositwin,text="account no:")
          accountnoLbel.grid(row="1",column="1")
          accountEntry=Entry(depositwin)
          accountEntry.grid(row="1",column="2")
          amountnoLbel=Label(depositwin,text="enter the amount:")
          amountnoLbel.grid(row="3",column="1")
          amountEntry=Entry(depositwin)
          amountEntry.grid(row="3",column="2")
          def deposi():
                account1=accountEntry.get()
                amount=amountEntry.get()
                deposit(account1,amount)
          depobutton=Button(depositwin,text="Deposit",command=deposi).grid(row="5",column="2")
          depositwin.mainloop()
      depositb=Button(menuwin,text="Deposit",command=depo).pack()
      def withdraww():
            withdrawin=Toplevel()
            accountnolabel=Label(withdrawin,text="enter the account no:")
            accountnolabel.grid(row="1",column="1")
            accountEntry1=Entry(withdrawin)
            accountEntry1.grid(row="1",column="2")
            amountnoLbel=Label(withdrawin,text="enter the amount:")
            amountnoLbel.grid(row="3",column="1")
            amountEntry1=Entry(withdrawin)
            amountEntry1.grid(row="3",column="2")
            def withdra():
                  account=accountEntry1.get()
                  amount=amountEntry1.get()
                  if Withdraw(account,amount):
                      messagebox.showinfo("Withdraw amount","amount withdrawn successfully")
                  else:messagebox.showerror("Withdraw amount","enter correct amount or account number")

            withdrawbutton=Button(withdrawin,text="withdraw",command=withdra).grid(row="5",column="2")
            withdrawin.mainloop()
      withdrawb=Button(menuwin,text="Withdraw",command=withdraww).pack()
      def bal():
            try:
                a=checkBal(accountNo.get())
                messagebox.showinfo("Balance",f"balance is:{a}")
            except:
                 messagebox.showerror("Balance","ERROR occured please try after some time!")
      checkbalb=Button(menuwin,text="Check balance",command=bal).pack()
      def changepass():
           changepasswin=Toplevel()
           passwlabel=Label(changepasswin,text="Enter password:")
           passwlabel.place(x="20",y="50",width="100")
           passwentry=Entry(changepasswin)
           passwentry.place(x="120",y="50",width="100")
           newpasswlabel=Label(changepasswin,text="Enter New-password:")
           newpasswlabel.place(x="20",y="100",width="100")
           newpasswentry=Entry(changepasswin)
           newpasswentry.place(x="120",y="100",width="100")
           renewpasswlabel=Label(changepasswin,text="Re-enter New-password:")
           renewpasswlabel.place(x="20",y="150",width="100")
           renewpasswentry=Entry(changepasswin)
           renewpasswentry.place(x="120",y="150",width="100")
           def changep():
                password1=passwentry.get()
                newpassword=newpasswentry.get()
                renewpassword=renewpasswentry.get()
                if newpassword==renewpassword:
                     try:
                        changepassword(accountNo.get(),password1,newpassword)
                        messagebox.showinfo("Update password","password updated successfully")
                     except:
                        messagebox.showerror("update password","couldn't update password")
           change=Button(changepasswin,text="change password",command=changep)
           change.place(x="70",y="200",width="70")
           changepasswin.mainloop()


      changepassb=Button(menuwin,text="change password",command=changepass).pack()
      menuwin.mainloop()
      


def newAcc():
    newAccwindow=Toplevel()
    newAccwindow.geometry("720x720")
    newAccwindow.title("Create New Account-ABC BANK")
    logo=PhotoImage(file="logo.png")
    newAccwindow.iconphoto(TRUE,logo)
    newAccwindow.config(background='#E7F0DC')
    image3=PhotoImage(file="abcBank 1.png")
    label3=Label(newAccwindow,image=image3,padx=30,pady=30)
    #label1.grid(row="0",column="2")
    label3.pack()
    
    userdetailsLabel=Label(newAccwindow,text='enter your details:',padx=10,pady=10)
    userdetailsLabel.pack()
    frame3=Frame(newAccwindow,padx=10,pady=10)
    frame3.pack()
    nameLabel=Label(frame3, text="Enter your name:")
    #nameLabel.place(x=20,y=15,width=25)
    nameLabel.grid(row="0",column="0")

    name = Entry(frame3)
    #name.place(x=20,y=15,width=25)
    name.grid(row="0",column="1")

    passwordLabel=Label(frame3, text="Enter password:")
    #passwordLabel.place(x=20,y=35,width=25)
    passwordLabel.grid(row="1",column="0")

    passwordentry= Entry(frame3)
    #passwordentry.place(x=20,y=15,width=25)
    passwordentry.grid(row="1",column="1")

    repasswordLabel=Label(frame3, text="Re-enter password:")
    #repasswordLabel.place()
    repasswordLabel.grid(row="2",column="0")

    repasswordentry= Entry(frame3)
    #repasswordentry.place()
    repasswordentry.grid(row="2",column="1")

    ageLabel=Label(frame3, text="Enter age:")
    #ageLabel.place(x=20,y=35,width=25)
    ageLabel.grid(row="3",column="0")

    ageEntry= Entry(frame3)
    #ageEntry.place(x=20,y=15,width=25)
    ageEntry.grid(row="3",column="1")

    addressLabel=Label(frame3, text="Enter your address:")
    addressLabel.grid(row="4",column="0")

    addressentry=Entry(frame3)
    addressentry.grid(row="4",column="1")

    aadharLabel=Label(frame3, text="Enter your Aadhar number:")
    aadharLabel.grid(row="5",column="0")

    aadharentry=Entry(frame3)
    aadharentry.grid(row="5",column="1")

    mobileLabel=Label(frame3, text="Enter your Mobile number:")
    mobileLabel.grid(row="6",column="0")

    mobileentry=Entry(frame3)
    mobileentry.grid(row="6",column="1")

    emailLabel=Label(frame3, text="Enter your email:")
    emailLabel.grid(row="7",column="0")

    emailentry=Entry(frame3)
    emailentry.grid(row="7",column="1")

    def new():
          Name=str(name.get())
          password=str(passwordentry.get())
          repassword=str(repasswordentry.get())
          age=int(ageEntry.get())
          address=str(addressentry.get())
          aadhar=str(aadharentry.get())
          mobile=str(mobileentry.get())
          email=str(emailentry.get())
          a= createNewAccount(Name,age,address,aadhar,email,password,mobile)
          messagebox.showinfo("Account Successfully created .\n", f"Account number is:{a}\n thank you ")
          #else: messagebox.showerror("Login Failed", "Invalid account number or password")
    button1=Button(newAccwindow,text="sign-in",command=new)
    button1.pack()

    newAccwindow.mainloop()

newAccbutton=Button(frame2,text="Create new Account",command=newAcc)
newAccbutton.grid(row="0",column="2")

mainWindow.mainloop()
