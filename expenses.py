import sys

sys.path.append(".")

from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox, Notebook
from tkinter_basics import tkinter_basics
from expenses_classes import index

def generate_expenses(): 
    ## declare exercise 1 and props
    _window = tkinter_basics(title='Inmobiliaria Software - Expensas', iconUrl='./assets/icon_inmo.ico')
    _window.can_resize(False)
    _window.root.config(background='#594A7D')
    _window.execute_window()

    expenses_object = index.Expenses_Page()


    def close_window () :
        '''
            close window
        '''
        _window.root.destroy()

    def minimize_window():
        '''
            minimize window
        '''
        _window.root.iconify()

    def browse_button():
        filename = filedialog.askdirectory()
        print(filename)
        return filename

    # Create Notebook panel
    notebook = Notebook(_window.root)
    notebook.config(width = 800, height = 500)
    notebook.grid(column=0, columnspan=11, sticky=W, row=0, rowspan=11, padx=3, pady=3) 


    # Create labels
    file_1 = Frame (notebook, bg='#594A7D')
    file_2 = Frame (notebook)


    # Add labels 
    notebook.add (file_1, text = "First exercise" ) 
    notebook.add (file_2, text = "Third exercise")