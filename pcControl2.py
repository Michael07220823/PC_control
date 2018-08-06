# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:04:30 2018

@author: michael
"""
import tkinter as tk
import os
root='root'
class PcControl():
    def __init__(self,master):
        master = tk.Tk()
        #master.geometry('300x300')
        master.title("PC Controler")
        master.resizable(0,0)
        frame = tk.Frame(master)
        frame.pack()
        
        self.btn1 = tk.Button(frame,text="Log_Out",width=10,command=self.logOut)
        #self.btn1.pack(side="left")
        self.btn1.grid(row=0,column=0,sticky='W')
        
        self.btn2 = tk.Button(frame,text="Lock",width=10,command=self.lock)
        #self.btn2.pack(side="left")
        self.btn2.grid(row=0,column=1,sticky='W')
        
        self.btn3 = tk.Button(frame,text="Power_Off",width=10,command=self.powerOff)
        #self.btn3.pack(side="left")
        self.btn3.grid(row=0,column=2,sticky='W')
        
        self.btn4 = tk.Button(frame,text="Reboot",width=10,command=self.reboot)
        #self.btn4.pack(side="left")
        self.btn4.grid(row=1,column=0,sticky='W')
        
        self.btn5 = tk.Button(frame,text="Deep_Sleep",width=10,command=self.deepSleep)
        #self.btn5.pack(side="left")
        self.btn5.grid(row=1,column=1,sticky='W')
        
        self.btn6 = tk.Button(frame,text="Exit",width=10,command=frame.quit)
        #self.btn6.pack(side="left")
        self.btn6.grid(row=1,column=2,sticky='W')
        
        self.lab1 = tk.Label(frame,text="Author：Overcomer_No.1",fg="red")
        #self.lab1.pack(side="bottom")
        #self.lab1.place(x=50,y=50,width=200,height=2)
        self.lab1.grid(rowspan=2,columnspan=3,sticky="S")
        
        master.mainloop()
        
    def logOut(self):
        os.system("shutdown -l")
        
    def deepSleep(self):
        os.system("shutdown -h")

    def powerOff(self):
        os.system("shutdown -s -t 0")
    
    def reboot(self):
        os.system("shutdown -r -t 0")
    
    def lock(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")
        
a = PcControl(root)
