from tkinter import*

def uno():
    import expensas as e
    e.generar_expensas()
    
    
def dos():
    import comprobante as c
    c.generar_comprobante()


def main ():
    root = Tk()

    root.title ('Inmobiliaria Software')
    root.geometry ("500x200")
    root.iconbitmap ('icon_inmo.ico')
    root.resizable (0, 0)
    root.config (bg = '#2B3A4A')

    block1 = Frame()
    block1.grid (row = 0, column = 0, columnspan = 2)
    block1.config (width = '500', height = '80', bg = '#15202B')
    python_image = PhotoImage (file = 'logo_inmo.png')
    label = Label (root, image = python_image, bg = '#15202B')
    label.grid (row = 0, column = 0, columnspan = 2)

    btn1 = Button (text = 'Generar Expensas', width = "20", command = uno, font = 'Cambria 12', bg = '#15202B', fg = 'white')
    btn1.grid (row = 1, column = 0, pady=40)

    btn1 = Button (text = 'Generar Comprobante', width = "20", command = dos, font = 'Cambria 12', bg = '#15202B', fg = 'white')
    btn1.grid (row = 1, column = 1)
    root.mainloop()


if __name__ == "__main__":
    main()


