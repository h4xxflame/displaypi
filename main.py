#!/usr/bin/python
from tkinter import *


class Display(Tk):

    def __init__(self):
        Tk.__init__(self)
        container = Tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = StartPage(container,vself)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Tk.frame):

    def __init__(self, parent, controller):
        Tk.Frame.__init__(self, parent)
        label = Tk.Label(self, text="asdasddas")
        #asdasd
        label.pack()


d = Display()
