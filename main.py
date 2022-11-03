import sys
from tkinter.ttk import Combobox
sys.path.append(".")
from tkinter import *
from tkinter_basics import tkinter_basics



def screen_expenses():
    import expenses as e
    e.generate_expenses()
   
    
    
def screen_generate_proof_payment():
    import proof_payment as pp
    pp.generate_proof_payment()

 
def main ():
    ej_3 = tkinter_basics()
    ej_3.can_resize(FALSE)
    ej_3.change_theme('dark')
    
    block1 = Frame()
    block1.grid (row = 0, column = 0, columnspan = 2)
    block1.config (width = '500', height = '80', bg = '#15202B')
    python_image = PhotoImage (file = './assets/logo_inmo.png')
    label = Label (image = python_image, bg = '#15202B')
    label.grid (row = 0, column = 0, columnspan = 2)
    

    btn1 = Button (text = 'Generar Expensas', width = "20", command = screen_expenses, font = 'Cambria 12', bg = '#15202B', fg = 'white')
    btn1.grid (row = 1, column = 0, pady=40)

    btn2 = Button (text = 'Generar Comprobante', width = "20", command = screen_generate_proof_payment, font = 'Cambria 12', bg = '#15202B', fg = 'white')
    btn2.grid (row = 1, column = 1)
    
    ej_3.execute_window()


if __name__ == "__main__":
    main()

