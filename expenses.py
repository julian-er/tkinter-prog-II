import sys

sys.path.append(".")

from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Combobox, Notebook
from tkinter_basics import tkinter_basics
from expenses_classes import consortium, index

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
    tenant = Frame (notebook, bg='#594A7D')
    expenses = Frame (notebook)


    # Add labels 
    notebook.add (tenant, text = "Datos Inquilino / Dueño" ) 
    notebook.add (expenses, text = "Expensas")

    ### TENANT NOTEBOOK ###
    # Get and store data
    name = StringVar()
    last_name = StringVar()

    # Labels
    name = Label(tenant, text="User : ", fg='#FFFFFF', background='#594A7D')
    name.grid(column=1, columnspan=2, sticky=W, row=1, rowspan=1, padx=3, pady=3)

    last_name = Label(tenant, text="Password : ", fg='#FFFFFF', background='#594A7D')
    last_name.grid(column=1, columnspan=2, sticky=W, row=5, rowspan=1, padx=3, pady=3)

    # Entries
    name_entry = Entry(tenant, textvariable=name)
    name_entry.grid(column=1, columnspan=2, sticky=EW, row=2, rowspan=1, padx=3, pady=3)

    last_name_entry = Entry(tenant, textvariable=last_name,  show='*')
    last_name_entry.grid(column=1, columnspan=2, sticky=EW, row=6, rowspan=1, padx=3, pady=3)


    # # TEST FOR CLASSES
    # # add expenses
    # expenses_object.add_expense('Tasa municipal', 'city_tax', 400)
    # expenses_object.add_expense('Tasa inmobiliaria', 'real_state_tax', 400)
    # # add consortium data
    # expenses_object.add_consortium('Adm. Lares', 'Santa Fe 6700. Rosario, Santa Fe, AR', '3413657899', 'adm_lares@lares.com', '20-09090-3', '3456723981237489023', 'Santader 4', 'tomas holder')
    # expenses_object.consortium.add_service('locksmith_phone', '7676767676')
    # # add tenant
    # expenses_object.add_tenant('Hernan', 'Gobu', 'Heras 5', 7, 35, 0)

    # print(expenses_object)