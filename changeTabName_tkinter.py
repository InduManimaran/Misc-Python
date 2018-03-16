import tkinter as tk
from tkinter import ttk
from tkinter import *

class Foo(tk.Frame):
    def __init__(self,master,notebook,name):
        tk.Frame.__init__(self,master)

        self.tabname=name
        page=ttk.Frame(notebook)
        
        notebook.add(page, text=self.tabname)

        button=Button(page, text="Change tab name", command=lambda: self.changeTabName(notebook,page))
        button.grid(row=1, column=1, sticky=N)

        notebook.pack()

    def changeTabName(self,notebook,page):
        index=notebook.index(notebook.select())
        notebook.tab(index,text="Tab Name Changed!!!")

class Bar:

    def __init__(self):
        self.root = tk.Tk()
        notebook=ttk.Notebook(self.root)
        obj1=Foo(self.root,notebook,"tab1")
        obj2=Foo(self.root,notebook,"tab2")


if __name__ == "__main__":
    Bar=Bar()
    Bar.root.mainloop()

