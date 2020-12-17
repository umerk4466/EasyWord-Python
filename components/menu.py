import tkinter as tk
import sys
from tkinter import messagebox

# Component of MenuBar
class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self)
        # menu
        self.menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu",underline=0, menu=self.menu)
        self.menu.add_command(label="Exit", underline=1, command=self.quit)
        # help
        self.helpManu = tk.Menu(self, tearoff=0,)
        self.add_cascade(label="Help",underline=0, menu=self.helpManu)
        self.helpManu.add_command(label="About", underline=1, command=self.showVersionInfo)

    # method to quit the program
    def quit(self):
        sys.exit(0)

    # method to show info about the program
    def showVersionInfo(self):
        messagebox.showinfo("About","EasyWords v.1 \n\nEasyWord is a dictionary software which will help you to find everything about the english word. \n\nFor more information email on umerk4466@gmail.com")
