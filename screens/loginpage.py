# tkinter modules
import tkinter as tk
from tkinter import messagebox
# import Main Page class
from screens.mainpage import MainPage
from screens.signuppage import SignupPage
from classes.user import User


# class for login page
class LoginPage(tk.Frame):
    def __init__(self, parent):
        # gui window settings
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Login To EasyWords v.1")
        # centering the window screen
        self.parent.geometry("{}x{}+{}+{}".format(680, 480, int((self.parent.winfo_screenwidth()/2) - (680/2)), int((self.parent.winfo_screenheight()/2) - (480/2))))
        self.parent.resizable(False, False)

        ##### components/widgets
        # top heading label
        self.welcomeLabel = tk.Label(self.parent, text="Welcome to the EasyWords", font=("Arial", 12))
        self.secondLabel = tk.Label(self.parent, text="Enter you credentials to login")
        # username
        self.usernameLabel = tk.Label(self.parent, text="Username")
        self.usernameEntry = tk.Entry(self.parent)
        # password
        self.passwordLabel = tk.Label(self.parent, text="Password ")
        self.passwordEntry = tk.Entry(self.parent, show="*", relief="groove")
        # login/Signup button
        self.loginBtn = tk.Button(self.parent, text = 'Login', relief="ridge", command = self.loginEvent)
        self.orLabel = tk.Label(self.parent, text="or")
        self.signupBtn = tk.Button(self.parent, text = 'Signup', relief="ridge", command = self.signupEvent)
        
        ##### layout
        # top heading label
        self.welcomeLabel.pack(pady=40)
        self.secondLabel.pack(pady=10)
        # username
        self.usernameLabel.pack()
        self.usernameEntry.pack()
        self.usernameEntry.focus()
        # password
        self.passwordLabel.pack()
        self.passwordEntry.pack()
        # login/Signup button
        self.loginBtn.pack(pady=20, ipadx=20)
        self.orLabel.pack()
        self.signupBtn.pack(pady=10, ipadx=25)
        
    # button event for signup
    def signupEvent(self):
        # open signup window
        topLavelWindow = tk.Toplevel(self.parent)
        window = SignupPage(topLavelWindow)
        window.mainloop()

    # button event for login
    def loginEvent(self):
        try:
            # create user object and validate
            user = User()
            user.setUsername(self.usernameEntry.get())
            user.setPassword(self.passwordEntry.get())
            if user.validate():
                self.parent.destroy()
                root = tk.Tk()
                app = MainPage(root,user)
                app.focus_force()
            else:
                messagebox.showerror("Login Failed!!!", "Somthing is wrong, could not login. Please check your username and password and try again.")
                self.secondLabel["text"] = "Incorrect username or password"
                self.secondLabel["fg"] = "red"
        except:
                messagebox.showwarning("Login Failed!!!", "Username and Password field can not be emplty, If you do not have account then press 'Signup' button to register.")
                self.secondLabel["text"] = "Username or password cannot be empty"
                self.secondLabel["fg"] = "red"
