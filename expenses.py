import sys

sys.path.append(".")

from tkinter import filedialog, ttk
from tkinter import *
from tkinter.ttk import Combobox, Notebook
from tkinter_basics import tkinter_basics
from expenses_classes import consortium, index

def generate_expenses(): 
    ## declare exercise 1 and props
    _window = tkinter_basics()
    _window.can_resize(False)
    _window.root.config(background='#15202B')
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
    notebook.grid(column=10, columnspan=11, sticky=W, row=0, rowspan=11, padx=3, pady=3) 


    # Create labels
    tenant = Frame (notebook, bg='#15202B')
    expenses = Frame (notebook, bg='#15202B')


    # Add labels 
    notebook.add (tenant, text = "Datos Inquilino / Dueño" ) 
    notebook.add (expenses, text = "Expensas")


    ### TENANT NOTEBOOK ###
    building_box = Label(tenant, text="Edificio :", font='Cambria 11', fg='#FFFFFF', background='#15202B')
    building_box.grid(column=0, row=0, sticky=E, pady=5)
    building_box = ttk.Combobox (tenant)
    building_box.grid (column = 1, row = 0, sticky = E)
    building_box ['values'] = ('1', '2', '3', '4', '5','6','7','8','9','10')
    building_box.set ('1')
    building_box.config (width = 17)

    name = Label(tenant, text="Nombre :", font='Cambria 11', fg='#FFFFFF', background='#15202B')
    name.grid(column=0, row=1, sticky=E, pady=5)
    name = StringVar()
    name_entry = Entry(tenant, textvariable=name)
    name_entry.grid(column=1, row=1)


    last_name = Label(tenant, text="Apellido :", font='Cambria 11', fg='#FFFFFF', background='#15202B')
    last_name.grid(column=0, row=2, sticky=E, pady=5)
    last_name = StringVar()
    last_name_entry = Entry(tenant, textvariable=last_name,  show='*')
    last_name_entry.grid(column=1, row=2)


    floor = Label(tenant, text="Piso :", font='Cambria 11', fg='#FFFFFF', background='#15202B')
    floor.grid(column=0, row=3, sticky=E, pady=5)
    floor = StringVar()
    floor_entry = Entry(tenant, textvariable=floor)
    floor_entry.grid(column=1, row=3)


    current_month = Label(tenant, text="Expensas mes corriente :", font='Cambria 11', fg='#FFFFFF', background='#15202B')
    current_month.grid(column=0, row=4, sticky=E, pady=5)
    current_month = StringVar()
    current_month_entry = Entry(tenant, textvariable=current_month)
    current_month_entry.grid(column=1, row=4)


    last_balance = Label(tenant, text="Saldo anterior :", font='Cambria 11', fg='#FFFFFF', background='#15202B')
    last_balance.grid(column=0, row=5, sticky=E, pady=5)
    last_balance = StringVar()
    last_balance_entry = Entry(tenant, textvariable=last_balance)
    last_balance_entry.grid(column=1, row=5)


    total_balance = Label(tenant, text="Total :", font='Cambria 11', fg='#FFFFFF', background='#15202B')
    total_balance.grid(column=0, row=6, sticky=E, pady=5)
    total_balance = StringVar()
    total_balance_entry = Entry(tenant, textvariable=total_balance)
    total_balance_entry.grid(column=1, row=6)



    ### EXPENSES NOTEBOOK ###
    city_tax = Label(expenses, text="Tasas Municipales :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    city_tax.grid(column=0, row=0, sticky=E)
    city_tax = StringVar()
    city_tax_entry = Entry(expenses, textvariable=city_tax)
    city_tax_entry.grid(column=1, row=0)


    real_state_tax = Label(expenses, text="Tasas Inmobiliarias :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    real_state_tax.grid(column=0, row=1, sticky=E)
    real_state_tax = StringVar()
    real_state_tax_entry = Entry(expenses, textvariable=real_state_tax)
    real_state_tax_entry.grid(column=1, row=1)


    water_tax = Label(expenses, text="Agua :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    water_tax.grid(column=0, row=2, sticky=E)
    water_tax = StringVar()
    water_tax_entry = Entry(expenses, textvariable=water_tax)
    water_tax_entry.grid(column=1, row=2)


    water_r_tax = Label(expenses, text="Agua (reserva) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    water_r_tax.grid(column=0, row=3, sticky=E)
    water_r_tax = StringVar()
    water_r_tax_entry = Entry(expenses, textvariable=water_r_tax)
    water_r_tax_entry.grid(column=1, row=3)


    water_r_tax = Label(expenses, text="Agua (reserva) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    water_r_tax.grid(column=0, row=4, sticky=E)
    water_r_tax = StringVar()
    water_r_tax_entry = Entry(expenses, textvariable=water_r_tax)
    water_r_tax_entry.grid(column=1, row=4)


    epe = Label(expenses, text="E.P.E :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    epe.grid(column=0, row=5, sticky=E)
    epe = StringVar()
    epe_entry = Entry(expenses, textvariable=epe)
    epe_entry.grid(column=1, row=5)


    epe_res = Label(expenses, text="E.P.E (reserva) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    epe_res.grid(column=0, row=6, sticky=E)
    epe_res = StringVar()
    epe_res_entry = Entry(expenses, textvariable=epe_res)
    epe_res_entry.grid(column=1, row=6)


    clean = Label(expenses, text="Limpieza :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    clean.grid(column=0, row=7, sticky=E)
    clean = StringVar()
    clean_entry = Entry(expenses, textvariable=clean)
    clean_entry.grid(column=1, row=7)


    clean_res = Label(expenses, text="Limpieza (reserva) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    clean_res.grid(column=0, row=8, sticky=E)
    clean_res = StringVar()
    clean_res_entry = Entry(expenses, textvariable=clean_res)
    clean_res_entry.grid(column=1, row=8)


    clean_art = Label(expenses, text="Limpieza (artículos) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    clean_art.grid(column=0, row=9, sticky=E)
    clean_art = StringVar()
    clean_art_entry = Entry(expenses, textvariable=clean_art)
    clean_art_entry.grid(column=1, row=9)


    clean_bonus = Label(expenses, text="Limpieza (aguinaldo) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    clean_bonus.grid(column=0, row=10, sticky=E)
    clean_bonus = StringVar()
    clean_bonus_entry = Entry(expenses, textvariable=clean_bonus)
    clean_bonus_entry.grid(column=1, row=10)


    lift = Label(expenses, text="Ascensor (mantenimiento) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    lift.grid(column=0, row=11, sticky=E)
    lift = StringVar()
    lift_entry = Entry(expenses, textvariable=lift)
    lift_entry.grid(column=1, row=11)


    maintenance = Label(expenses, text="Mantenimiento (reserva) :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    maintenance.grid(column=0, row=12, sticky=E)
    maintenance = StringVar()
    maintenance_entry = Entry(expenses, textvariable=maintenance)
    maintenance_entry.grid(column=1, row=12)


    security = Label(expenses, text="Seguridad :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    security.grid(column=0, row=13, sticky=E)
    security = StringVar()
    security_entry = Entry(expenses, textvariable=security)
    security_entry.grid(column=1, row=13)


    bookstore_item = Label(expenses, text="Artículos de librería :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    bookstore_item.grid(column=0, row=14, sticky=E)
    bookstore_item = StringVar()
    bookstore_item_entry = Entry(expenses, textvariable=bookstore_item)
    bookstore_item_entry.grid(column=1, row=14)

    
    provident = Label(expenses, text="Fondo de previsión :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    provident.grid(column=0, row=15, sticky=E)
    provident = StringVar()
    provident_entry = Entry(expenses, textvariable=provident)
    provident_entry.grid(column=1, row=15)


    build_insurance = Label(expenses, text="Seguro R.C. Prop. Horizontal :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    build_insurance.grid(column=0, row=16, sticky=E)
    build_insurance = StringVar()
    build_insurance_entry = Entry(expenses, textvariable=build_insurance)
    build_insurance_entry.grid(column=1, row=16)


    banking = Label(expenses, text="Gastos bancarios mensuales :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    banking.grid(column=0, row=17, sticky=E)
    banking = StringVar()
    banking_entry = Entry(expenses, textvariable=banking)
    banking_entry.grid(column=1, row=17)


    issues_insurance = Label(expenses, text="Seguro accidentes personales :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    issues_insurance.grid(column=0, row=18, sticky=E)
    issues_insurance = StringVar()
    issues_insurance_entry = Entry(expenses, textvariable=issues_insurance)
    issues_insurance_entry.grid(column=1, row=18)


    fee = Label(expenses, text="Honorarios administración :", font='Cambria 10 bold', fg='#FFFFFF', background='#15202B')
    fee.grid(column=0, row=19, sticky=E)
    fee = StringVar()
    fee_entry = Entry(expenses, textvariable=fee)
    fee_entry.grid(column=1, row=19)



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