# tkinter modules
import tkinter as tk
from tkinter import messagebox
# import Main Page class
from classes.user import User


# class for signupPage
class SignupPage(tk.Frame):
    def __init__(self, parent):
        # gui window settings
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Signup With EasyWords v.1")
        # centering the windows
        self.parent.geometry("{}x{}+{}+{}".format(340, 420, int((self.parent.winfo_screenwidth()/2) - (340/2)), int((self.parent.winfo_screenheight()/2) - (420/2))))
        self.parent.resizable(False, False)
        
        ##### components/widgets
        # top heading label
        self.welcomeLabel = tk.Label(self.parent, text="Signup With EasyWords", font=("Arial", 12))
        self.secondLabel = tk.Label(self.parent, text="To signup fill the below given fields")
        # email
        self.emailLabel = tk.Label(self.parent, text="Enter Your Email*")
        self.emailEntry = tk.Entry(self.parent)
        # username
        self.usernameLabel = tk.Label(self.parent, text="Enter Username*")
        self.usernameEntry = tk.Entry(self.parent)
        # password
        self.passwordLabel = tk.Label(self.parent, text="Enter Password*")
        self.passwordEntry = tk.Entry(self.parent, show="*", relief="groove")
        # back to signup button
        self.signupBtn = tk.Button(self.parent, text = 'Signup Now', relief="ridge", command=self.signupNowEvent)
        
        ##### layout
        # top heading label
        self.welcomeLabel.pack(pady=40)
        self.secondLabel.pack(pady=10)
        # email
        self.emailLabel.pack()
        self.emailEntry.pack()
        self.emailEntry.focus()
        # username
        self.usernameLabel.pack()
        self.usernameEntry.pack()
        # password
        self.passwordLabel.pack()
        self.passwordEntry.pack()
        # back to signup button
        self.signupBtn.pack(pady=20, ipadx=20)

    # button event for signup
    def signupNowEvent(self):
        # create user object and register new user
        try:
            user = User()
            user.setUsername(self.usernameEntry.get())
            user.setPassword(self.passwordEntry.get())
            user.setEmailAddress(self.emailEntry.get())
            user.signup()
            messagebox.showinfo("Signup Successful", "Congratulations, Your account has been made successfully. Now login")
            self.parent.destroy()
        except:
            messagebox.showerror("Signup Failed!!!", "Something is wrong, Please fill all the required fields.", parent=self.parent)
            self.secondLabel["text"] = "Please fill all the required fields"
            self.secondLabel["fg"] = "red"