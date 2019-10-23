#!/usr/bin/python2
# coding: utf-8

from tkinter import *
from search import *

town1 = "Bordeaux"
town2 = "Marseille"

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.input_town1 = Entry(self)
        self.input_town1.pack(side="left")

        self.input_town2 = Entry(self)
        self.input_town2.pack(side="right")


        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.print_input)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def print_input(self):
        print(self.input_town1.get())
        print(self.input_town2.get())

root = Tk()
app = Application(master=root)
app.mainloop()




















#    window = Tk()

#    Frame1 = Frame(window, borderwidth=2, relief=GROOVE)
#    Frame1.pack(side=BOTTOM, padx=60, pady=60)

#    Frame3 = Frame(window, borderwidth=2, relief=GROOVE)
#    Frame3.pack(side=TOP, padx=10, pady=10)

#    times = time_compute()

#    value = StringVar()
#    value.set("texte par défaut")
#    entree = Entry(Frame1, textvariable='string', width=30)
#    entree.pack(side=LEFT, padx=5, pady=5)
#    print(entree.get())

#    value2 = StringVar()
#    value2.set("texte par défaut")
#    entree2 = Entry(Frame1, textvariable='string', width=30)
#    entree.pack(side=RIGHT, padx=5, pady=5)

#    Label(Frame3, bg='#3385ff', text=" Ville de Départ ", borderwidth=1, relief=GROOVE).grid(row=1, column=1)
#    Label(Frame3, bg='#3385ff', text=" Ville d'arrivé ", borderwidth=1, relief=GROOVE).grid(row=1, column=2)
#    Label(Frame3, bg='#3385ff', text=" Temps de trajet total ", borderwidth=1, relief=GROOVE).grid(row=1, column=3)
#    Label(Frame3, bg='#ffff99', text=town1, borderwidth=1, relief=FLAT).grid(row=2, column=1)
#    Label(Frame3, bg='#ffff99', text=town2, borderwidth=1, relief=FLAT).grid(row=2, column=2)
#    Label(Frame3, bg='#ffff99', text=times, borderwidth=1, relief=FLAT).grid(row=2, column=3)
#    window.mainloop()