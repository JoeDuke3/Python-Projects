#!/usr/bin/python
#-*- coding: utf-8 -*-

# IMPORTS
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# MODULES
import app_gui
import app_func

"""
window = Tk()

lframe=Frame(window)
lbox=Listbox(lframe,height=10)
lbox.pack(side=LEFT)
scroll=Scrollbar(lframe,orient=VERTICAL)
scroll.pack(side=LEFT)
scroll=configure(command=lbox.yview)
lb.configure(yscrollcommand=scroll.set)
"""

# PARENT WINDOW "FRAME" CLASS
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # MASTER FRAME CONFIGURATION
        self.master = master
        self.master.minsize(600,600)
        self.master.maxsize(600,600)
        # CENTER THE WINDOW
        app_func.center_window(self,600,600)
        self.master.title("Academy Student Tracker")
        self.master.configure(bg = "#353")
        # CATCH A CLICK ON X
        self.master.protocol("WM_DELETE_WINDOW", lambda: app_func.ask_quit(self))
        arg = self.master

        # LOAD THE GUI FROM A SEPERATE MODULE
        app_gui.load_gui(self)

        # DROPDOWN MENU
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", underline = 1, accelerator = "Ctrl+Q", command = lambda: app_func.ask_quit(self))
        menubar.add_cascade(label = "File", underline = 0, menu = filemenu)
        self.master.config(menu = menubar, borderwidth = '1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
