from tkinter import *
from tkinter import ttk
from table import Table


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
        self.table1 = Table(self.tab1, 'postgres', True)

        # Creating second table in
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Table 2")
        self.table2 = Table(self.tab2, 'mysql', False)
        Button(self.tab2, text="Export to Table 2", command=self.export_to_table2).grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
       
        # Creating third table in
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Table 3")
        self.table3 = Table(self.tab3, 'sqlite', False)
        Button(self.tab3, text="Export to Table 3", command=self.export_to_table3).grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
        
        
    def export_to_table2(self):
        data = self.table1.db.select_all()
        self.table2.db.truncate()
        for row in data:
            self.table2.db.insert(row)
        self.table2.refresh()

    
    def export_to_table3(self):
        data = self.table2.db.export_query()
        self.table3.db.truncate()
        for row in data:
            self.table3.db.insert(row)
        self.table3.refresh()


if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()