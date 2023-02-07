#!/usr/bin/env python3

import tkinter as tk
import operator
import math
# from tkinter import ttk

def plus(a,b):
    return a+b

opr2 = {"+" : plus, "-" : lambda a,b: b-a, "*" : lambda a,b: a*b,"/" : operator.truediv,  "//" : lambda a,b: a//b,  "%" : lambda a,b: a%b}
opr1={"V": math.sqrt, "sin": math.sin, "cos": math.cos, "tg": math.tan, }
cons={"pi": math.pi, "e": math.e,}

class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if "textvariable" not in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = "Foo"
    title_ = "Reverse calculator"
    geometry_="250x324"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.title_)
        self.geometry(self.geometry_)
        self.bind("<Escape>", self.quit)
        self.entry = MyEntry(self)
        self.entry.pack(side="top", fill="x")


        self.frame1=tk.Frame(self)
        self.frame1.pack(fill="both")
        self.listbox = tk.Listbox(self.frame1)
        self.listbox.pack(side="left", fill="y")
        self.frame2= tk.Frame(self.frame1)
        self.frame2.pack(side="right", fill="y")

        self.button1=tk.Button(self.frame2, text="🡅")
        self.button1.pack(side="top", ipadx=20, ipady=5)
        self.button1.bind("<ButtonRelease-1>", self.UP)

        self.button2=tk.Button(self.frame2, text="🡇")
        self.button2.pack(side="top", ipadx=20, ipady=5)
        self.button2.bind("<ButtonRelease-1>", self.DOWN)

        self.button3=tk.Button(self.frame2, text="delete")
        self.button3.pack(side="bottom", ipadx=20, ipady=5)
        self.button3.bind("<ButtonRelease-1>", self.DELETE)

        self.button4=tk.Button(self.frame2, text="copy")
        self.button4.pack(side="bottom", ipadx=20, ipady=5)
        self.button4.bind("<ButtonRelease-1>", self.COPY)

        self.label1= tk.Label(self, text="")
        self.label1.pack(side="bottom", fill="x",)

       

        self.entry.bind("<Return>", self.process)
        self.entry.bind("<KP_Enter>", self.process)

        self.listbox.bind("<ButtonRelease-1>", self.onclick)

    def onclick(self, event:tk.Event):
        print(self.listbox.get("anchor"))
        print(self.listbox.get("active"))
        print(self.listbox.curselection())

    def UP(self, event:tk.Event):
        index = self.listbox.curselection()[0]
        cislo = self.listbox.get(index)
        self.listbox.insert(index -1,cislo)
        self.listbox.delete(index+1)

    def DOWN(self, event:tk.Event):
        index = self.listbox.curselection()[0]
        cislo = self.listbox.get(index)
        self.listbox.insert(index +2,cislo)
        self.listbox.delete(index)

    def DELETE(self, event:tk.Event):
        index = self.listbox.curselection()[0]
        self.listbox.delete(index)
    def COPY(self, event:tk.Event):
        index = self.listbox.curselection()[0]
        cislo = self.listbox.get(index)
        self.listbox.insert(index +1,cislo)


    def process(self, e: tk.Event):
        line = self.entry.value
        for token in line.split():
            self.process_token(token)
        self.entry.value = ""

    def process_token(self, token:str):
        try:
            try:
                token = token.replace(",", ".")
                number=float(token)
                self.listbox.insert(0, number)
            except ValueError:
                if token in opr2:
                    a= self.listbox.get(0)
                    self.listbox.delete(0)
                    b= self.listbox.get(0)
                    self.listbox.delete(0)
                    self.listbox.insert(0, opr2[token](a,b))
                if token in opr1:
                    a= self.listbox.get(0)
                    self.listbox.delete(0)
                    self.listbox.insert(0, opr1[token](a,b))
                if token in cons:
                    self.listbox.insert(0, cons[token])
        except:
            self.label1.config(text="chyba")


        

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()


