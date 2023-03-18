from tkinter import *
from tkinter import ttk
from table import Table

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Tables")
        self.root.geometry("620x380")

        # Creating notebook widget
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Creating first table in first tab
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Table 1")
        self.table1 = Table(self.tab1, True)

        # Creating second table in
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Table 2")
        self.table2 = Table(self.tab2, False)
        Button(self.tab2, text="Export to Table 2", command=self.export_to_table2).grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
        
       
        # Creating third table in
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Table 3")
        self.table3 = Table(self.tab3, False)
        Button(self.tab3, text="Export to Table 3", command=self.export_to_table3).grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
        
        
    def export_to_table2(self):
        for item in self.table1.tree.get_children():
            id = self.table1.tree.item(item, "values")[0]
            name = self.table1.tree.item(item, "values")[1]
            age = self.table1.tree.item(item, "values")[2]
            self.table2.tree.insert("", "end", values=(id, name, age))

    
    def export_to_table3(self):
        for item in self.table1.tree.get_children():
            id = self.table1.tree.item(item, "values")[0]
            name = self.table1.tree.item(item, "values")[1]
            age = self.table1.tree.item(item, "values")[2]
            self.table3.tree.insert("", "end", values=(id, name, age))


if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()