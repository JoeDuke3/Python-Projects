#!/usr/bin/python  
# -*- coding: utf-8 -*-

# IMPORTS
import tkinter as tk
from tkinter import *

# MODULES
import app_main
import app_func

# GUI
def load_gui(self):
    # LISTBOX/SCROLLBAR WIDGETS
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection = 0, yscrollcommand = self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: app_func.onSelect(self,event))
    self.scrollbar1.config(command = self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=1,rowspan=10,columnspan=1,padx=(5,5),pady=(5,5),sticky=N+S)
    self.lstList1.grid(row=1,column=0,rowspan=10,columnspan=1,padx=(5,5),pady=(5,5),sticky=N+E+W+S)

    self.lbl_KGBimeanNSA = tk.Label(self.master, font = ("Cascadia Code", 15), bg = "#353", fg = "#ccc", text = 'JUST GIVE US THE INFORMATION, COMRADE...')
    self.lbl_KGBimeanNSA.grid(row=0,column=0,columnspan=4,padx=(5,5),pady=(5,5),sticky=E+W)
    self.lbl_fname = tk.Label(self.master, font = ("Cascadia Code", 15), bg = "#353", fg = "#ccc", text = 'FIRST NAME')
    self.lbl_fname.grid(row=1,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.lbl_lname = tk.Label(self.master, font = ("Cascadia Code", 15), bg = "#353", fg = "#ccc", text = 'LAST NAME')
    self.lbl_lname.grid(row=3,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.lbl_phone = tk.Label(self.master, font = ("Cascadia Code", 15), bg = "#353", fg = "#ccc", text = 'PHONE NUMBER')
    self.lbl_phone.grid(row=5,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.lbl_email = tk.Label(self.master, font = ("Cascadia Code", 15), bg = "#353", fg = "#ccc", text = 'EMAIL ADDRESS')
    self.lbl_email.grid(row=7,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.lbl_course = tk.Label(self.master, font = ("Cascadia Code", 15), bg = "#353", fg = "#ccc", text = 'CURRENT COURSE')
    self.lbl_course.grid(row=9,column=3,padx=(5,5),pady=(5,5),sticky=E+W)

    self.txt_fname = tk.Entry(self.master, font = ("Cascadia Code", 15), bg = "#333", fg = "#ccc",)
    self.txt_fname.grid(row=2,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.txt_lname = tk.Entry(self.master, font = ("Cascadia Code", 15), bg = "#333", fg = "#ccc",)
    self.txt_lname.grid(row=4,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.txt_phone = tk.Entry(self.master, font = ("Cascadia Code", 15), bg = "#333", fg = "#ccc",)
    self.txt_phone.grid(row=6,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.txt_email = tk.Entry(self.master, font = ("Cascadia Code", 15), bg = "#333", fg = "#ccc",)
    self.txt_email.grid(row=8,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    self.txt_course = tk.Entry(self.master, font = ("Cascadia Code", 15), bg = "#333", fg = "#ccc",)
    self.txt_course.grid(row=10,column=3,padx=(5,5),pady=(5,5),sticky=E+W)
    
    self.btn_add = tk.Button(self.master, width = 12, height = 2, font = ("Impact", 15), bg = "#666", fg = "#0f0", text = 'UPDATE', command = lambda: app_func.updateList(self))
    self.btn_add.grid(row=11,column=3,padx=(5,5),pady=(5,5),sticky=N)
    self.btn_del = tk.Button(self.master, width = 12, height = 2, font = ("Impact", 15), bg = "#666", fg = "#f00", text = 'DELETE', command = lambda: app_func.onDelete(self))
    self.btn_del.grid(row=11,column=0,padx=(5,5),pady=(5,5),sticky=N)

    app_func.create_db(self)
    app_func.onRefresh(self)
    
if __name__ == "__main__":
    pass
