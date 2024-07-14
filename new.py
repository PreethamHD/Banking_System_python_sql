from account import *
from customtkinter import *
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
from dataChecker import *

set_default_color_theme('blue')
mainWindow=CTk()
# Main login window 
mainWindow.geometry("460x400")
mainWindow.title("Login-ABC BANK")
label=CTkLabel(mainWindow,text="ABC Bank ",font=("calibri",30),text_color="#5e17eb")
label.pack()

image12=ImageTk.PhotoImage(Image.open("abcbank111.jpg"))
label1=CTkLabel(mainWindow,image=image12,text="")
label1.pack()

#Frame that has account no label and entry and password label and entry
frame=CTkFrame(mainWindow,width=450,height=450)
frame.pack(pady=40)

accountLabel=CTkLabel(frame, text="Enter account no:",pady=30)
accountLabel.grid(row="1",column="1")

accountNo = CTkEntry(frame)
accountNo.grid(row="1",column="2",columnspan="3")

passLabel=CTkLabel(frame, text="Enter password :",pady=30)
passLabel.grid(row="3",column="1")

Password = CTkEntry(frame,show='*')
Password.grid(row="3",column="2",columnspan=3)

frame2=CTkFrame(mainWindow,width=500,height=500)
frame2.pack()

aN=accountNo.get()
#Function that gets the data from account entry and password entry and checks if thry are valid and if valid calls the function login1(AccountNo,Password) from account.py
def login():
        passwordB=Password.get()
        AccountNo=accountNo.get()
        if isaccountNo(AccountNo): 
            if login1(AccountNo,passwordB):
                messagebox.showinfo("succesfully logged in","login successfull!")
                #mainWindow.destroy()
                menu()
                
                
            else:messagebox.showerror("Login Failed", "Invalid password")
        else: messagebox.showerror("Login Failed", "Invalid account number")

loginB=CTkButton(frame2,text="Login",command=login)
loginB.grid(row="0",column="0",padx=10)

aN=accountNo.get()

#Menu function creates the menu window that has deposit, withdraw, check balance, delete account, change password and performs the functions
def menu():
      menuwin=CTk()
      menuwin.geometry("460x400")
      menuwin.title("Services-ABC BANK")

      menuFrame=CTkFrame(menuwin)
      menuFrame.place(relx=0.5,rely=0.5,anchor=CENTER)
      
      label=CTkLabel(menuwin,text="services:",font=("arial",18))
      label.place(relx=0.3,rely=0.3,anchor=CENTER)
      
      def depo():
          depositwin=CTk()
          depositwin.geometry("360x300")
          deposiFrame=CTkFrame(depositwin)
          deposiFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

          accountnoLbel=CTkLabel(deposiFrame,text="Account Number:")
          accountnoLbel.grid(row="1",column="1",pady=10)
          accountEntry=CTkEntry(deposiFrame)
          accountEntry.grid(row="1",column="2",pady=10)

          amountnoLbel=CTkLabel(deposiFrame,text="Amount:")
          amountnoLbel.grid(row="3",column="1",pady=10)
          amountEntry=CTkEntry(deposiFrame)
          amountEntry.grid(row="3",column="2",pady=10)

          #Function that checks if the entered amount and account no is valid and if yes calls the function deposit() from account.py
          def deposi():
                account1=accountEntry.get()
                amount=amountEntry.get()

                if isaccountNo(account1)==False:
                     messagebox.showerror("invalid Account Number","Enter the Valid Account Number")
                     return
                if isAmount(amount) and isaccountNo(account1):
                   deposit(account1,amount)
                   messagebox.showinfo("Success",f"{amount} deposited successfully")
                   depositwin.destroy()
                else:messagebox.showerror("invalid amount","Enter valid Amount")
                         
          depobutton=CTkButton(deposiFrame,text="Deposit",command=deposi)
          depobutton.grid(row="5",column="1",columnspan="2",pady=10)

          depositwin.mainloop()
      depositb=CTkButton(menuFrame,text="Deposit",command=depo)
      depositb.grid(row="1",column="1",padx="10",pady="10")

      def withdraww():
            withdrawin=CTk()
            withdrawin.geometry("360x300")

            withdrawFrame=CTkFrame(withdrawin)
            withdrawFrame.place(relx=0.5,rely=0.5,anchor=CENTER)

            accountnolabel=CTkLabel(withdrawFrame,text="Account No:")
            accountnolabel.grid(row="1",column="1",pady=10)
            accountEntry1=CTkEntry(withdrawFrame)
            accountEntry1.grid(row="1",column="2",pady=10)

            amountnoLbel=CTkLabel(withdrawFrame,text="Amount:")
            amountnoLbel.grid(row="3",column="1",pady=10)
            amountEntry1=CTkEntry(withdrawFrame)
            amountEntry1.grid(row="3",column="2",pady=10)

            #Function that validates the account no and amount and calls Withdraw() from account.py which handles sql part of the code
            def withdra():
                  account=accountEntry1.get()
                  amount=amountEntry1.get()

                  if isaccountNo(account) and isAmount(amount):
                       if Withdraw(account,amount):
                             messagebox.showinfo("Withdraw amount","amount withdrawn successfully")
                             withdrawin.destroy()
                       else:messagebox.showerror("Withdraw amount","enter correct amount or account number")
                  else: messagebox.showerror("Error","Enter valid Account Number or Amount")

            withdrawbutton=CTkButton(withdrawFrame,text="withdraw",command=withdra).grid(row="5",column="1",columnspan="2",pady=10)
            withdrawin.mainloop()

      withdrawb=CTkButton(menuFrame,text="Withdraw",command=withdraww)
      withdrawb.grid(row="1",column="2",padx="10",pady="10")

      def bal():
            try:
                a=checkBal(accountNo.get())
                messagebox.showinfo("Balance",f"balance is:{a}")
            except:
                 messagebox.showerror("Balance","ERROR occured please try after some time!")

      checkbalb=CTkButton(menuFrame,text="Check balance",command=bal)
      checkbalb.grid(row="2",column="1",padx="10",pady="10")

      def changepass():
           changepasswin=CTk()
           changepasswin.geometry("360x300")
           frame1=CTkFrame(changepasswin)
           frame1.place(relx=0.5,rely=0.5,anchor=CENTER)

           passwlabel=CTkLabel(frame1,text="Enter password:")
           passwlabel.grid(row="1",column="1",pady=10)
           passwentry=CTkEntry(frame1)
           passwentry.grid(row="1",column="2",pady=10)

           newpasswlabel=CTkLabel(frame1,text="Enter New-password:")
           newpasswlabel.grid(row="2",column="1",pady=10)
           newpasswentry=CTkEntry(frame1)
           newpasswentry.grid(row="2",column="2",pady=10)

           renewpasswlabel=CTkLabel(frame1,text="Re-enter New-password:")
           renewpasswlabel.grid(row="3",column="1",pady=10)
           renewpasswentry=CTkEntry(frame1)
           renewpasswentry.grid(row="3",column="2",pady=10)

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
           change=CTkButton(frame1,text="change password",command=changep)
           change.grid(row="4",column="1",columnspan="2",pady=10)
           changepasswin.mainloop()


      changepassb=CTkButton(menuFrame,text="change password",command=changepass)
      changepassb.grid(row="2",column="2",padx="10",pady="10")

      def dele():
           delewin=CTk()
           delewin.geometry("360x300")
           frame11=CTkFrame(delewin)
           frame11.place(relx=0.5,rely=0.5,anchor=CENTER)

           def dela():
                balen=deleteAcc(accountNo.get())
                if balen>0:
                     messagebox.showinfo("Delete Account",f"Account successfully deleted and {balen} rupees issued")
                elif balen==0:messagebox.showinfo("Delete account","Account successfully Deleted")
                else:messagebox.showerror("Error","Couldn't Delete Account")
                     
           yesB=CTkButton(frame11,text="yes",command=dela)
           yesB.grid(row="0",column="0")
           def destr():
                delewin.destroy()
           noB=CTkButton(frame11,text="no",command=destr)
           noB.grid(row="0",column="1")
           delewin.mainloop()
      deleteAccountB=CTkButton(menuFrame,text="Delete Account",command=dele)
      deleteAccountB.grid(row="3",column="1",columnspan="2",pady=10)
      menuwin.mainloop()
      
def newAcc():
    newAccwindow=CTk()
    newAccwindow.geometry("720x720")
    newAccwindow.title("Create New Account-ABC BANK")
    
    label3=CTkLabel(newAccwindow,text="",padx=30,pady=30)
    label3.pack()
    
    userdetailsLabel=CTkLabel(newAccwindow,text='Enter your details:',font=("calibri",28),text_color="blue",padx=10,pady=10)
    userdetailsLabel.pack()

    frame3=CTkFrame(newAccwindow)
    frame3.pack(pady=30)

    nameLabel=CTkLabel(frame3, text="Enter your name:")
    nameLabel.grid(row="0",column="0",pady=10)
    name = CTkEntry(frame3)
    name.grid(row="0",column="1",pady=10)

    passwordLabel=CTkLabel(frame3, text="Enter password:")
    passwordLabel.grid(row="1",column="0",pady=10)
    passwordentry= CTkEntry(frame3)
    passwordentry.grid(row="1",column="1",pady=10)

    repasswordLabel=CTkLabel(frame3, text="Re-enter password:")
    repasswordLabel.grid(row="2",column="0",pady=10)
    repasswordentry= CTkEntry(frame3)
    repasswordentry.grid(row="2",column="1",pady=10)

    ageLabel=CTkLabel(frame3, text="Enter age:")
    ageLabel.grid(row="3",column="0",pady=10)
    ageEntry= CTkEntry(frame3)
    ageEntry.grid(row="3",column="1",pady=10)

    addressLabel=CTkLabel(frame3, text="Enter your address:")
    addressLabel.grid(row="4",column="0",pady=10)
    addressentry=CTkEntry(frame3)
    addressentry.grid(row="4",column="1",pady=10)

    aadharLabel=CTkLabel(frame3, text="Enter your Aadhar number:")
    aadharLabel.grid(row="5",column="0",pady=10)
    aadharentry=CTkEntry(frame3)
    aadharentry.grid(row="5",column="1",pady=10)

    mobileLabel=CTkLabel(frame3, text="Enter your Mobile number:")
    mobileLabel.grid(row="6",column="0",pady=10)
    mobileentry=CTkEntry(frame3)
    mobileentry.grid(row="6",column="1",pady=10)

    emailLabel=CTkLabel(frame3, text="Enter your email:")
    emailLabel.grid(row="7",column="0",pady=10)
    emailentry=CTkEntry(frame3)
    emailentry.grid(row="7",column="1",pady=10)

    def new():
          Name=str(name.get())
          password=str(passwordentry.get())
          repassword=str(repasswordentry.get())
          age=ageEntry.get()
          address=str(addressentry.get())
          aadhar=str(aadharentry.get())
          mobile=str(mobileentry.get())
          email=str(emailentry.get())

          if isName(Name) and isAddress(address) and isAadhar(aadhar) and isMobile(mobile) and isEmail(email) and isAge(age):
               #Function createNewAccount() creates the account and returns the account number
               a= createNewAccount(Name,age,address,aadhar,email,password,mobile)
               messagebox.showinfo("Account Successfully created .\n", f"Account number is:{a}\n thank you ")
          else: messagebox.showerror("Error", "Enter Valid Details")
          newAccwindow.destroy()
          
    button1=CTkButton(newAccwindow,text="sign-in",command=new)
    button1.pack()

    newAccwindow.mainloop()

newAccbutton=CTkButton(frame2,text="Create new Account",command=newAcc)
newAccbutton.grid(row="0",column="4",padx=10)
mainWindow.mainloop()