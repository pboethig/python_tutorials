#!/usr/lib/python2.7

from Tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        self.contents = StringVar()
        self.contents.set("this is a variable")
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>', self.print_contents)


    def print_contents(self, event):
        print "hi. contents of entry is now ---->", \
            self.contents.get()



myApp = App()

myApp.master.title("My Do nothig app")
myApp.master.maxsize(1000,400)
myApp.master.minsize(1000, 400);

myApp.mainloop()