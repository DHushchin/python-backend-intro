from tkinter import *
from tkinter import ttk
from table import MongoTable


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Tables")
        self.root.geometry("520x440")

        # Creating notebook widget
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Creating first table in first tab
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Table 1")
        self.table1 = MongoTable(self.tab1, 'mongodb', True)

if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()