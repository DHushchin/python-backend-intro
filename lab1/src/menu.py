from tkinter import *
from tkinter import ttk

class Table:
    def __init__(self, parent):
        self.parent = parent

        # Creating columns
        columns = ("#1", "#2", "#3")
        self.tree = ttk.Treeview(self.parent, columns=columns, show="headings")

        # Assigning column names
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Name")
        self.tree.heading("#3", text="Age")

        # Adding sample data to table
        self.tree.insert("", "end", values=("1", "John Doe", "30"))
        self.tree.insert("", "end", values=("2", "Jane Smith", "25"))
        self.tree.insert("", "end", values=("3", "Bob Johnson", "40"))

        # Adding table to window
        self.tree.pack(pady=10)

        # Creating entry fields
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()

        Label(self.parent, text="ID:").pack()
        Entry(self.parent, textvariable=self.id_var).pack()

        Label(self.parent, text="Name:").pack()
        Entry(self.parent, textvariable=self.name_var).pack()

        Label(self.parent, text="Age:").pack()
        Entry(self.parent, textvariable=self.age_var).pack()

        # Creating buttons for CRUD operations
        Button(self.parent, text="Add", command=self.add).pack(pady=5)
        Button(self.parent, text="Update", command=self.update).pack(pady=5)
        Button(self.parent, text="Delete", command=self.delete).pack(pady=5)


    def add(self):
        id = self.id_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        self.tree.insert("", "end", values=(id, name, age))


    def update(self):
        selected = self.tree.selection()
        for item in selected:
            self.tree.item(item, values=(self.id_var.get(), self.name_var.get(), self.age_var.get()))

  
    def delete(self):
        selected = self.tree.selection()
        for item in selected:
            self.tree.delete(item)


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Tables")
        self.root.geometry("1000x600")

        # Creating notebook widget
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill=BOTH)

        # Creating first table in first tab
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Table 1")
        self.table1 = Table(self.tab1)

        # Creating second table in second tab
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Table 2")
        self.table2 = Table(self.tab2)
        Button(self.tab2, text="Export to Table 2", command=self.export_to_table2).pack(pady=10)

        # Creating third table in third tab
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Table 3")
        self.table3 = Table(self.tab3)
        Button(self.tab3, text="Export to Table 3", command=self.export_to_table3).pack(pady=10)

   
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
