from tkinter import *
from tkinter import ttk


class Table:
    def __init__(self, parent, crud : bool):
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
        self.tree.grid(row=0, column=0, columnspan=3, padx=0, pady=0)

        if not crud:
            return
            
        # Creating entry fields
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.age_var = StringVar()
        Label(self.parent, text="ID:").grid(row=1, column=1, padx=10, pady=5, sticky="w")
        Entry(self.parent, textvariable=self.id_var).grid(row=1, column=1, padx=5, pady=5)
        Label(self.parent, text="Name:").grid(row=2, column=1, padx=10, pady=5, sticky="w")
        Entry(self.parent, textvariable=self.name_var).grid(row=2, column=1, padx=10, pady=5)
        Label(self.parent, text="Age:").grid(row=3, column=1, padx=10, pady=5, sticky="w")
        Entry(self.parent, textvariable=self.age_var).grid(row=3, column=1, padx=10, pady=5)
        # Creating buttons for CRUD operations
        Button(self.parent, text="Add", command=self.add).grid(row=1, column=1, padx=10, pady=5, sticky="e")
        Button(self.parent, text="Update", command=self.update).grid(row=2, column=1, padx=10, pady=5, sticky="e")
        Button(self.parent, text="Delete", command=self.delete).grid(row=3, column=1, padx=10, pady=5, sticky="e")


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


