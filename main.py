import tkinter as tk
from screens.loginpage import LoginPage

# define main function
def main(): 
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()


if __name__ == '__main__':
    main()