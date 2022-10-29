from tkinter import*

def expenses():
    import expenses as e
    e.generate_expenses()
    
    
def proof_payment():
    import proof_payment as p
    p.generate_proof_payment()


def main ():
    root = Tk()

    root.title ('Inmobiliaria Software')
    root.geometry ("500x200")
    root.iconbitmap ('icon_real estate.ico')
    root.resizable (0, 0)
    root.config (bg = '#2B3A4A')

    block1 = Frame()
    block1.grid (row = 0, column = 0, columnspan = 2)
    block1.config (width = '500', height = '80', bg = '#15202B')
    python_image = PhotoImage (file = 'logo_real estate.png')
    label = Label (root, image = python_image, bg = '#15202B')
    label.grid (row = 0, column = 0, columnspan = 2)

    btn_expenses = Button (text = 'Generar Expensas', width = "20", command = expenses, font = 'Cambria 12', bg = '#15202B', fg = 'white')
    btn_expenses.grid (row = 1, column = 0, pady=40)

    btn_proof_payment = Button (text = 'Generar Comprobante', width = "20", command = proof_payment, font = 'Cambria 12', bg = '#15202B', fg = 'white')
    btn_proof_payment.grid (row = 1, column = 1)
    
    root.mainloop()


if __name__ == "__main__":
    main()


