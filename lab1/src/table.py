from tkinter import *
from tkinter import ttk

from db.factory_db import DBFactory


class Table:
    def __init__(self, parent, db_name : str, crud : bool):
        self.parent = parent
        self.db = DBFactory().get_db(db_name)
        self.__table_gui()

        if crud:
            self.__crud_gui()
        
        
    def __table_gui(self):
        # Creating columns
        columns = self.db.get_columns()
        self.tree = ttk.Treeview(self.parent, columns=columns, show="headings")

        # Assigning column names
        for column in columns:
            self.tree.heading(column, text=column.title())
            self.tree.column(column, width=100, anchor="center")

        # Adding table to window
        self.tree.grid(row=0, column=0, columnspan=3, padx=0, pady=0)
        
        # Getting data from database
        self.get_data() 
         
                       
    def __crud_gui(self):
        # Creating entry fields
        self.data_entry = []
        for i, column in enumerate(self.db.get_columns()):
            Label(self.parent, text=column.title()).grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
            setattr(self, f"{column}_var", StringVar())
            self.data_entry.append(getattr(self, f"{column}_var"))
            Entry(self.parent, textvariable=getattr(self, f"{column}_var")).grid(row=i+1, column=1, padx=10, pady=5, sticky="w")

        
        # Creating buttons for CRUD operations
        Button(self.parent, text="Add", command=self.add).grid(row=1, column=2, padx=10, pady=5, sticky="nsew")
        Button(self.parent, text="Update", command=self.update).grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
        Button(self.parent, text="Delete", command=self.delete).grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
        
        
    def get_data(self):
        data = self.db.select_all()
        if data:
            for row in data:
                self.tree.insert("", "end", values=row)


    def add(self):
        data = [var.get() for var in self.data_entry]
        self.db.insert(data)
        self.tree.insert("", "end", values=data)
        self.clear_entry()


    def update(self):
        data = [var.get() for var in self.data_entry]
        self.db.update(data)
        self.refresh()
        self.clear_entry()
  
  
    def delete(self):
        selected = self.tree.selection()
        for item in selected:
            _id = self.tree.item(item, "values")[0]
            self.tree.delete(item)
            self.db.delete(_id)
            
            
    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.get_data()
     
        
    def clear_entry(self):
        for var in self.data_entry:
            var.set("")
