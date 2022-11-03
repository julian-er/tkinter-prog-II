import PySimpleGUI as sg
from pathlib import Path
from docxtpl import DocxTemplate
import datetime

sg.theme('DarkGrey14')

def generate_expenses(): 
    
    doc = DocxTemplate('expenses.docx')
    today = datetime.datetime.today()

    # Datos inquilino
    frame_tenant_info = [

        [sg.Text("Nombre y Apellido:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="TENANT",size=40, do_not_clear=False)],
        
        [sg.Text("Edificio:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="BUILDING",size=40)],
        
        [sg.Text("Piso:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="FLOOR",size=10, do_not_clear=False)],

        [sg.Text("Expensas Mes Corriente ($):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CURRENT_MONTH",size=10, do_not_clear=False)],
        
        [sg.Text("Saldo Anterior ($):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="LAST_BALANCE",size=10, do_not_clear=False)],

        [sg.Text("Recargo Segundo Vencimiento (%):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="INTEREST",size=10, do_not_clear=False)],

        [sg.Text("Mes:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="MONTH",size=10, do_not_clear=False)],
        
        [sg.Text("Año:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="YEAR",size=10, do_not_clear=False)],

    ]

    # Datos consorcio
    frame_building_info = [

        [sg.Text("Direccion Administración:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="ADDRESS",size=40)],
        
        [sg.Text("Telefono Administración:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="PHONE",size=40)],
        
        [sg.Text("Horario Atención:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="HOURS",size=40)],

        [sg.Text("Mail:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="EMAIL",size=40)],

        [sg.Text("Nombre Titular Cuenta Bancaria:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="ACCOUNT_HOLDER",size=40)],
        
        [sg.Text("Cuit:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CUIT",size=40)],

        [sg.Text("CBU:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CBU",size=40)],

        [sg.Text("Sucursal:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="BANK_BRANCH",size=40)],

        [sg.Text("Cerrajero:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="LOCKSMITH_PHONE",size=40)],

        [sg.Text("Hidráulico:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="HYDRAULIC_PHONE",size=40)],

        [sg.Text("Electricista:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="ELECTRICIAN_PHONE",size=40)],

        [sg.Text("Ascensor:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="LIFT_PHONE",size=40)],

    ]

    # Datos Impuestos
    frame_taxes = [

        [sg.Text("Proporcional:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="T_PROP",size=15)],

        [sg.Text("Tasas Municipales:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CITY_TAX",size=15)],
        
        [sg.Text("Tasa Inmobiliario:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="REAL_STATE_TAX",size=15)],
        
        [sg.Text("Agua:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="WATER_TAX",size=15)],

        [sg.Text("Agua (reserva):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="WATER_R_TAX",size=15)],
        
        [sg.Text("E.P.E. Servicio:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="EPE",size=15)],
        
        [sg.Text("E.P.E. (reserva):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="EPE_RES",size=15)],

        [sg.Text("Limpieza Servicio:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CLEAN",size=15)],

        [sg.Text("Limpieza (reserva):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CLEAN_RES",size=15)],

        [sg.Text("Limpieza (artículos):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CLEAN_ART",size=15)],

        [sg.Text("Limpieza (aguinaldo):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="CLEAN_BONUS",size=15)],

        [sg.Text("Ascensor Mantenimiento:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="LIFT",size=15)],
        
        [sg.Text("Mantenimiento (reserva):", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="MANTENAINCE",size=15)],

        [sg.Text("Servicios de Seguridad:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="SECURITY",size=15)],

        [sg.Text("Articulos de Librería:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="BOOKSTORE_ITEM",size=15)],

        [sg.Text("Fondo de Previsión:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="PROVIDENT",size=15)],

        [sg.Text("Seguro R.C. Propiedad Horizontal:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="BUILD_INSURANCE",size=15)],

        [sg.Text("Gastos Bancarios mensuales:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="BANKING",size=15)],

        [sg.Text("Seguro Acc. Personales:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="ISSUES_INSURANCE",size=15)],

        [sg.Text("Honorarios Administración:", font='Calibri 12 bold', background_color="#3A424F", pad=5), sg.Input(key="FEE",size=15)],
        
        [sg.Text("Comentarios", font='Calibri 14 bold', background_color="#3A424F"), sg.Multiline(key="COMMENTS", do_not_clear=False, size=(30, 5))],
    ]
    

    expenses_Col = [[sg.Column(frame_taxes, scrollable=True, vertical_scroll_only=True, background_color="#3A424F",element_justification="right")]]
    # Se incluyen en el layout principal los Tabs:  frame_datos_inquilino / frame_datos_consorcio / frame_impuestos
    layout = [
        
        [sg.TabGroup([
                        [sg.Tab("Datos Inquilino", frame_tenant_info, element_justification="right", background_color="#3A424F")],
                        [sg.Tab("Datos Consorcio", frame_building_info, element_justification="right", background_color="#3A424F")],
                        [sg.Tab("Impuestos", expenses_Col, element_justification="right", background_color="#3A424F")],
                        
                    ])
        ]
        
        ]

    layout +=[
        
        [sg.Button("RESET", font="Calibri 13 bold", key='-CLEAR-', button_color="#E04C5E"), sg.Button("EXPENSAS", font='Calibri 13 bold')],
    ]


    window = sg.Window("Inmobiliaria Software", layout, margins=(50,30), element_justification="right",background_color="#3A424F")
    
    

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
                values["TOTAL_BALANCE"] = round(float(values['CURRENT_MONTH'])) + round(float(values['LAST_BALANCE']))
                values["INTEREST"] = round(float(values['TOTAL_BALANCE'])) + round(float(values['TOTAL_BALANCE'])) * round(float(values['INTEREST']) / 100, 2)
                values["TODAY"] = today.strftime("%d-%m-%Y")
                values["FIRST_DATE_1"] = first_date_1.strftime("%d-%m-%Y")
                values["FIRST_DATE_2"] = first_date_2.strftime("%d-%m-%Y")
                values["SECOND_DATE_1"] = second_date_1.strftime("%d-%m-%Y")
                values["SECOND_DATE_2"] = second_date_2.strftime("%d-%m-%Y")

                #PROPORTIONALS
                values["P1"] = str(round(float(values["CITY_TAX"])) / round(float(values["T_PROP"])))
                values["P2"] = str(round(float(values["REAL_STATE_TAX"])) / round(float(values["T_PROP"])))
                values["P3"] = str(round(float(values["WATER_TAX"])) / round(float(values["T_PROP"])))
                values["P4"] = str(round(float(values["WATER_R_TAX"])) / round(float(values["T_PROP"])))
                values["P5"] = str(round(float(values["EPE"])) / round(float(values["T_PROP"])))
                values["P6"] = str(round(float(values["EPE_RES"])) / round(float(values["T_PROP"])))

                values["P7"] = str(round(float(values["CLEAN"])) / round(float(values["T_PROP"])))
                values["P8"] = str(round(float(values["CLEAN_RES"])) / round(float(values["T_PROP"])))
                values["P9"] = str(round(float(values["CLEAN_ART"])) / round(float(values["T_PROP"])))
                values["P10"] = str(round(float(values["CLEAN_BONUS"])) / round(float(values["T_PROP"])))
                values["P11"] = str(round(float(values["LIFT"])) / round(float(values["T_PROP"])))
                values["P12"] = str(round(float(values["MANTENAINCE"])) / round(float(values["T_PROP"])))

                values["P13"] = str(round(float(values["SECURITY"])) / round(float(values["T_PROP"])))
                values["P14"] = str(round(float(values["BOOKSTORE_ITEM"])) / round(float(values["T_PROP"])))
                values["P15"] = str(round(float(values["PROVIDENT"])) / round(float(values["T_PROP"])))
                values["P16"] = str(round(float(values["BUILD_INSURANCE"])) / round(float(values["T_PROP"])))
                values["P17"] = str(round(float(values["BANKING"])) / round(float(values["T_PROP"])))
                values["P18"] = str(round(float(values["ISSUES_INSURANCE"])) / round(float(values["T_PROP"])))
                values["P19"] = str(round(float(values["FEE"])) / round(float(values["T_PROP"])))

                #Render the template, save new word document & inform user
                del values[0]
                doc.render(values)
                output_path = Path(__file__).parent / f"{values['TENANT']}-expensas-{values['MONTH']} .docx"
                doc.save(output_path)
                sg.popup("Archivo Registrado", f"El archivo se guardo en la ruta: {output_path}")
                
        
    window.close()