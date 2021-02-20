#!/usr/bin/python
# -*- coding: utf-8 -*-

# IMPORTS
import os
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox

# MODULES
import app_main
import app_gui


# CENTER WINDOW
def center_window(self, w, h):
    # GET SCREEN DIMENSIONS
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # DO THE MATH
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# CATCH X CLICK AND MAKE SURE
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # CLOSE APP
        self.master.destroy()
        os._exit(0)

#==========================================================================

# CREATE DATABASE
def create_db(self):
    # CONNECT TO DATABASE
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_students(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_fname TEXT,\
            col_lname TEXT,\
            col_fullname TEXT,\
            col_phone TEXT,\
            col_email TEXT,\
            col_course TEXT\
            );")
        # COMMIT DATA AND CLOSE DATABASE
        conn.commit()
    conn.close()
    first_run(self)

# POPULATE THE LIST THE FIRST TIME APP OPENS
def first_run(self):
    data = ('John', 'Doe', 'John Doe', '555-555-5555', 'name@site.com', 'Python')
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students(col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""",(data))
            conn.commit()
    conn.close()

# COUNT NUMBER OF RECORD ENTRIES IN DATABASE
def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count

# SELECT ITEM IN LISTBOX
def onSelect(self, event):
    # lstList1 WIDGET IS CALLING HERE
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_course FROM tbl_students WHERE col_fullname = (?)""",[value])
        varBody = cur.fetchall()
        # SLICE RETURNED TUPLE INTO 5 PARTS
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def updateList(self):
    # GET AND SCRUB THE DATA
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname))
    var_phone = self.txt_phone.get()
    var_email = self.txt_email.get()
    var_course = self.txt_course.get()
    var_phone = var_phone.strip()
    var_email = var_email.strip()
    var_course = var_course.strip()
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('students.db')
        with conn:
            cur = conn.cursor()
            # CHECK FOR FULLNAME
            cur.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
            count = cur.fetchone()[0]
            # CHECK NEGATIVE/ADD
            if count == 0:
                cur.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""",(var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                # UPDATE LISTBOX
                self.lstList1.insert(END, var_fullname)
            # CHECK POSITIVE/UPDATE
            else:
                cur.execute("""UPDATE tbl_students SET col_phone = '{0}', col_email = '{1}', col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_phone, var_email, var_course, var_fullname))
            conn.commit()
        conn.close()
        onClear(self)
    else:
        messagebox.showerror("Missing information","Please fill all fields")

# DELETE SELECTION
def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        # CHECK TO MAKE SURE THIS DOESN'T EMPTY THE DATABASE
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        # CHECK OK
        if count > 1:
            # ASK IF SURE
            confirm= messagebox.askokcancel("Delete Confirmation", "All information associated with ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            # IF SURE
            if confirm:
                conn = sqlite3.connect('students.db')
                with conn:
                    cur = conn.cursor()
                    # DELETE
                    cur.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                # CLEAR TEXTBOXES
                onClear(self)
                # UPDATE LISTBOX
                onRefresh(self)
                # COMMIT CHANGES
                conn.commit()
            # CHECK NOT OK
        else:
            messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select))
    conn.close()

# CLEAR TEXTBOXES
def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

# UPDATE THE LISTBOX
def onRefresh(self):
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()


if __name__ == "__main__":
    pass
