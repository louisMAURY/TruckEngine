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
        self.createWidgets()
        self.master.title("Calcul Routier")

    def createWidgets(self):
        self.grid(row=0, column=0, sticky='nsew')

        self.lab_town1 = Label(self, text="Ville de départ")
        self.lab_town1.grid(row=1, column=1)

        self.lab_town2 = Label(self, text="Ville d'arrivé")
        self.lab_town2.grid(row=1, column=2)

        self.input_town1 = Entry(self, width=20)
        self.input_town1.grid(row=2, column=1)

        self.input_town2 = Entry(self, width=20)
        self.input_town2.grid(row=2, column=2)

        self.on_road = Button(self, text="En route", fg="Blue", command=self.letsGo)
        self.on_road.grid(row=2, column=3)

        self.to_excel = Button(self, text="Exporter dans un tableur", fg="Green", command=self.tablor)
        self.to_excel.grid(row=2, column=4)

        self.lab_start = Label(self, text="Ville de départ", borderwidth=1, width=20, bg="#66b3ff", relief="groove")
        self.lab_start.grid(row=4, column=1)

        self.lab_end = Label(self, text="Ville d'arrivé", borderwidth=1, width=20, bg="#66b3ff", relief="groove")
        self.lab_end.grid(row=4, column=2)

        self.lab_time = Label(self, text="Temps de trajet", borderwidth=1, width=20, bg="#66b3ff", relief="groove")
        self.lab_time.grid(row=4, column=3)

        self.lab_start2 = Label(self, text="________", borderwidth=1, width=20, bg="#b3d9ff", relief="flat")
        self.lab_start2.grid(row=6, column=1)

        self.lab_end2 = Label(self, text="________", borderwidth=1, width=20, bg="#b3d9ff", relief="flat")
        self.lab_end2.grid(row=6, column=2)

        self.lab_time2 = Label(self, text="________", borderwidth=1, width=20, bg="#b3d9ff", relief="flat")
        self.lab_time2.grid(row=6, column=3)

    def printInput(self):
        print(self.input_town1)
        print(self.input_town2.get())
        print(towns(self.input_town1, self.input_town2))

    def letsGo(self):
        start_town = self.input_town1.get().capitalize()
        end_town = self.input_town2.get().capitalize()
        dat_link = towns(start_town, end_town)
        webToFile(dat_link)
        the_distance = parsFile("workfile.html")
        self.lab_start2["text"] = start_town
        self.lab_end2["text"]= end_town
        self.lab_time2["text"] = timeCompute(the_distance)
        return timeCompute(the_distance)

    def tablor(self):
        starteuh = self.input_town1.get()
        endeuh = self.input_town2.get()
        writeInTab("roadboard.ods", starteuh, endeuh)


root = Tk()
root.geometry("700x150-300+300")
app = Application(master=root)
app.mainloop()
