import PySimpleGUI as sg
from pathlib import Path
from docxtpl import DocxTemplate
import datetime

sg.theme('DarkGrey14')

def generate_proof_payment():
    
    doc = DocxTemplate('proof_payment.docx')

    today = datetime.datetime.today()

    frame_proof_payment = [

        # Tenant info
        [sg.Text("Edificio:", font='Calibri 12 bold'), sg.Input(key="BUILDING", do_not_clear=False)],

        [sg.Text("Recibí del Sr./a:", font='Calibri 12 bold'), sg.Input(key="TENANT", do_not_clear=False)],
        
        [sg.Text("Unidad:", font='Calibri 12 bold'), sg.Input(key="FLOOR", do_not_clear=False)],

        # Month amount 
        [sg.Text("Expensas Mes Corriente ($):", font='Calibri 12 bold'), sg.Input(key="CURRENT_MONTH", do_not_clear=False)],
        
        # Month
        [sg.Text("Mes:", font='Calibri 12 bold'), sg.Input(key="MONTH", do_not_clear=False)],
    
        # Year
        [sg.Text("Año:", font='Calibri 12 bold'), sg.Input(key="YEAR", do_not_clear=False)],

        # Administrator name
        [sg.Text("Administrador:", font='Calibri 12 bold'), sg.Input(key="ADMINISTRATOR", do_not_clear=False)],        
    ]


    # Proof_payment frame is included in the layout
    layout = [
            [sg.Frame('Comprobante', frame_proof_payment, font='Calibri 14 bold',element_justification="right")],
            [sg.Button("RESET", size=15, font="Calibri 12 bold", key='-CLEAR-', button_color="#E04C5E"), sg.Button("COMPROBANTE", size=15, font='Calibri 12 bold')],
            ]

    window = sg.Window("Inmobiliaria Software", layout, margins=(20,20), element_justification="center")
    
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "COMPROBANTE":
            answer=sg.PopupYesNo(f"Desea generar el comprobante de {values['TENANT']}?")
            if answer == 'No':
                sg.WIN_CLOSED
            else:
                # Render the template, save new word document & inform user
                values["TODAY"] = today.strftime("%d-%m-%Y")
                doc.render(values)
                output_path = Path(__file__).parent / f"{values['TENANT']}-payment-{values['MONTH']} .docx"
                doc.save(output_path)
                sg.popup("Comprobante Registrado", f"El archivo se guardo en la ruta: {output_path}")

            
    window.close()