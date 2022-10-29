import PySimpleGUI as sg
from pathlib import Path
from docxtpl import DocxTemplate
import datetime

sg.theme('DarkGrey14')

def generar_comprobante():
    
    doc = DocxTemplate('comprobante.docx')

    today = datetime.datetime.today()


    frame_comprobante = [

        [sg.Text("Edificio:", font='Calibri 12 bold'), sg.Input(key="EDIFICIO", do_not_clear=False)],

        [sg.Text("Recibí del Sr./a:", font='Calibri 12 bold'), sg.Input(key="CLIENTE", do_not_clear=False)],
        
        [sg.Text("Unidad:", font='Calibri 12 bold'), sg.Input(key="UNIDAD", do_not_clear=False)],


        # Montos del mes 
        [sg.Text("Expensas Mes Corriente ($):", font='Calibri 12 bold'), sg.Input(key="MES_CORRIENTE", do_not_clear=False)],
        

        # mes corriente
        [sg.Text("Mes:", font='Calibri 12 bold'), sg.Input(key="MES", do_not_clear=False)],
    
        # Año corriente
        [sg.Text("Año:", font='Calibri 12 bold'), sg.Input(key="ANIO", do_not_clear=False)],

        [sg.Text("Administrador:", font='Calibri 12 bold'), sg.Input(key="ADMINISTRADOR", do_not_clear=False)],

        # Botón
        
    ]


    # se incluye en el layout frame_comprobante
    layout = [
            [sg.Frame('Comprobante', frame_comprobante, font='Calibri 14 bold',element_justification="right")],
            [sg.Button("RESET", size=15, font="Calibri 12 bold", key='-CLEAR-', button_color="#E04C5E"), sg.Button("COMPROBANTE", size=15, font='Calibri 12 bold')],
            ]

    window = sg.Window("Inmobiliaria Software", layout, margins=(20,20), element_justification="center")
    
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "COMPROBANTE":
            answer=sg.PopupYesNo(f"Desea generar el comprobante de {values['CLIENTE']}?")
            if answer == 'No':
                sg.WIN_CLOSED
            else:
                #Render the template, save new word document & inform user
                values["TODAY"] = today.strftime("%d-%m-%Y")
                doc.render(values)
                output_path = Path(__file__).parent / f"{values['CLIENTE']}-expensas-{values['MES']} .docx"
                doc.save(output_path)
                sg.popup("Comprobante Registrado", f"El archivo se guardo en la ruta: {output_path}")

            
    window.close()