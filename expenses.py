import PySimpleGUI as sg
from pathlib import Path
from docxtpl import DocxTemplate
import datetime

sg.theme('DarkGrey14')

def generate_expenses():
    
    doc = DocxTemplate('expenses.docx')

    today = datetime.datetime.today()

    
    frame_tenant_info = [

        [sg.Text("Nombre y Apellido:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="TENANT", do_not_clear=False)],
        
        [sg.Text("Edificio:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="BUILDING", do_not_clear=False)],
        
        [sg.Text("Piso:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="FLOOR", do_not_clear=False)],
 
        [sg.Text("Expensas Mes Corriente ($):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CURRENT_MONTH", do_not_clear=False)],
        
        [sg.Text("Saldo Anterior ($):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="LAST_BALANCE", do_not_clear=False)],

        [sg.Text("Recargo Segundo Vencimiento (%):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="INTEREST", do_not_clear=False)],

        [sg.Text("Mes:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="MONTH", do_not_clear=False)],
        
        [sg.Text("Año:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="YEAR", do_not_clear=False)],

    ]

    frame_real_state_info = [

        [sg.Combo(values=('Edificio 1', 'Edificio 2', 'Edificio 3'), default_value='EDIFICIO', readonly=False, k='BUILDING')],

        [sg.Text("Direccion Administración:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ADDRESS", do_not_clear=False)],
        
        [sg.Text("Telefono Administración:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="PHONE", do_not_clear=False)],
        
        [sg.Text("Horario Atención:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="HOURS", do_not_clear=False)],

        [sg.Text("Mail:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="EMAIL", do_not_clear=False)],

        [sg.Text("Nombre Titular Cuenta Bancaria:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ACCOUNT_HOLDER", do_not_clear=False)],
        
        [sg.Text("Cuit:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CUIT", do_not_clear=False)],

        [sg.Text("CBU:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CBU", do_not_clear=False)],

        [sg.Text("Sucursal:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="BANK_BRANCH", do_not_clear=False)],

        [sg.Text("Cerrajero:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="LOCKSMITH_PHONE", do_not_clear=False)],

        [sg.Text("Hidráulico:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="HYDRAULIC_PHONE", do_not_clear=False)],

        [sg.Text("Electricista:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ELECTRICIAN_PHONE", do_not_clear=False)],

        [sg.Text("Ascensor:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="LIFT_PHONE", do_not_clear=False)],

    ]

    frame_taxes = [

        [sg.Text("Proporcional:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="T_PROP", do_not_clear=False)],

        [sg.Text("Tasas Municipales:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CITY_TAX", do_not_clear=False)],
        
        [sg.Text("Tasa Inmobiliario:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="REAL_STATE_TAX", do_not_clear=False)],
        
        [sg.Text("Agua:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="WATER_TAX", do_not_clear=False)],

        [sg.Text("Agua (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="WATER_R_TAX", do_not_clear=False)],
        
        [sg.Text("E.P.E. Servicio:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="EPE", do_not_clear=False)],
        
        [sg.Text("E.P.E. (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="EPE_RES", do_not_clear=False)],

        [sg.Text("Limpieza Servicio:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CLEAN", do_not_clear=False)],

        [sg.Text("Limpieza (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CLEAN_RES", do_not_clear=False)],

        [sg.Text("Limpieza (artículos):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CLEAN_ART", do_not_clear=False)],

        [sg.Text("Limpieza (aguinaldo):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CLEAN_BONUS", do_not_clear=False)],

        [sg.Text("Ascensor Mantenimiento:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="LIFT", do_not_clear=False)],
        
        [sg.Text("Mantenimiento (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="MANTENAINCE", do_not_clear=False)],

        [sg.Text("Servicios de Seguridad:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="SECURITY", do_not_clear=False)],

        [sg.Text("Articulos de Librería:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="BOOKSTORE_ITEM", do_not_clear=False)],

        [sg.Text("Fondo de Previsión:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="PROVIDENT", do_not_clear=False)],

        [sg.Text("Seguro R.C. Propiedad Horizontal:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="BUILD_INSURANCE", do_not_clear=False)],

        [sg.Text("Gastos Bancarios mensuales:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="BANKING", do_not_clear=False)],

        [sg.Text("Seguro Acc. Personales:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ISSUES_INSURANCE", do_not_clear=False)],

        [sg.Text("Honorarios Administración:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="FEE", do_not_clear=False)],

        [sg.Text("Comentarios", font='Calibri 12 bold', background_color="#3A424F")],
        [sg.Multiline (size=(90, 3))],

        [sg.Button("RESET", font="Calibri 13 bold", key='-CLEAR-', button_color="#E04C5E"), sg.Button("EXPENSAS", font='Calibri 13 bold')],
        
    ]

    # rent_info, real_state_info and tax frames are included in the layout
    layout = [
        
        [sg.TabGroup([
                        [sg.Tab("Datos Inquilino", frame_tenant_info, element_justification="right", background_color="#3A424F")],
                        [sg.Tab("Datos Consorcio", frame_real_state_info, element_justification="right", background_color="#3A424F")], 
                        [sg.Tab("Impuestos", frame_taxes, element_justification="right", background_color="#3A424F")],
                        
                    ])
        ]
        
        ]

    window = sg.Window("Inmobiliaria Software", layout, margins=(50,20), element_justification="right")

    # Setting current date and expiration dates
    today = datetime.datetime.today()
    first_date_1 = today + datetime.timedelta(days=5)
    first_date_2 = today + datetime.timedelta(days=30)
    second_date_1 = today + datetime.timedelta(days=30)
    second_date_2 = today + datetime.timedelta(days=40)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "EXPENSAS":
            answer=sg.PopupYesNo(f"Registrar expensas de {values['TENANT']}?")
            if answer == 'No':
                sg.WIN_CLOSED
            else:
                # Add calculated fields to our dict
                values["TOTAL_BALANCE"] = round(float(values['LAST_BALANCE'])) + round(float(values['CURRENT_MONTH']))
                values["TOTAL_INTEREST_BALANCE"] = round(float(values['TOTAL_BALANCE'])) + round(float(values['TOTAL_BALANCE'])) * round(float(values['INTEREST']) / 100, 2)
                values["TODAY"] = today.strftime("%d-%m-%Y")
                values["FIRST_DATE_1"] = first_date_1.strftime("%d-%m-%Y")
                values["FIRST_DATE_2"] = first_date_2.strftime("%d-%m-%Y")
                values["SECOND_DATE_1"] = second_date_1.strftime("%d-%m-%Y")
                values["SECOND_DATE_2"] = second_date_2.strftime("%d-%m-%Y")

                

                # Render the template, save new word document & inform user
                doc.render(values)
                output_path = Path(__file__).parent / f"{values['TENANT']}-expensas-{values['MONTH']} .docx"
                doc.save(output_path)
                sg.popup("Archivo Registrado", f"El archivo se guardo en la ruta: {output_path}")
                


    window.close()