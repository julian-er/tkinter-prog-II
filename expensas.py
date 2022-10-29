import PySimpleGUI as sg
from pathlib import Path
from docxtpl import DocxTemplate
import datetime

sg.theme('DarkGrey14')

def generar_expensas():
    
    doc = DocxTemplate('expensas.docx')

    today = datetime.datetime.today()

    # Datos inquilino
    frame_datos_inquilino = [

        [sg.Text("Nombre y Apellido:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CLIENTE", do_not_clear=False)],
        
        [sg.Text("Edificio:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="EDIFICIO", do_not_clear=False)],
        
        [sg.Text("Piso:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="PISO", do_not_clear=False)],


        # Montos del mes 
        [sg.Text("Expensas Mes Corriente ($):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="MES_CORRIENTE", do_not_clear=False)],
        
        [sg.Text("Saldo Anterior ($):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="SALDO_ANTERIOR", do_not_clear=False)],

        # Recargo
        [sg.Text("Recargo Segundo Vencimiento (%):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="RECARGO_2", do_not_clear=False)],
        

        # Mes corriente
        [sg.Text("Mes:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="MES", do_not_clear=False)],
        
        # Año corriente
        [sg.Text("Año:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ANIO", do_not_clear=False)],

    ]

    # Datos consorcio
    frame_datos_consorcio = [

        [sg.Combo(values=('Edificio 1', 'Edificio 2', 'Edificio 3'), default_value='EDIFICIO', readonly=False, k='EDIFICIO')],

        [sg.Text("Direccion Administración:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="DIRECCION_ADMIN", do_not_clear=False)],
        
        [sg.Text("Telefono Administración:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="TELEFONO_ADMIN", do_not_clear=False)],
        
        [sg.Text("Horario Atención:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ATENCION_ADMIN", do_not_clear=False)],

        [sg.Text("Mail:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="MAIL_ADMIN", do_not_clear=False)],

        [sg.Text("Nombre Titular Cuenta Bancaria:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="TITULAR_ADMIN", do_not_clear=False)],
        
        [sg.Text("Cuit:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CUIT_ADMIN", do_not_clear=False)],

        [sg.Text("CBU:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CBU_ADMIN", do_not_clear=False)],

        [sg.Text("Sucursal:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="SUCURSAL_ADMIN", do_not_clear=False)],

        [sg.Text("Cerrajero:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="CERRAJERO", do_not_clear=False)],

        [sg.Text("Hidráulico:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="HIDRAULICO", do_not_clear=False)],

        [sg.Text("Electricista:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ELECTRICISTA", do_not_clear=False)],

        [sg.Text("Ascensor:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="ASCENSOR", do_not_clear=False)],

    ]

    # Datos Impuestos
    frame_impuestos = [

        [sg.Text("Proporcional:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="T_PROP", do_not_clear=False)],

        [sg.Text("Tasas Municipales:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="T_MUNIC", do_not_clear=False)],
        
        [sg.Text("Tasa Inmobiliario:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="T_INMO", do_not_clear=False)],
        
        [sg.Text("Agua:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="T_AGUA", do_not_clear=False)],

        [sg.Text("Agua (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="T_RES_AGUA", do_not_clear=False)],
        
        [sg.Text("E.P.E. Servicio:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_EPE", do_not_clear=False)],
        
        [sg.Text("E.P.E. (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_EPE_RES", do_not_clear=False)],

        [sg.Text("Limpieza Servicio:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_LIMPIEZA", do_not_clear=False)],

        [sg.Text("Limpieza (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_LIMPIEZA_RES", do_not_clear=False)],

        [sg.Text("Limpieza (artículos):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_LIMPIEZA_ART", do_not_clear=False)],

        [sg.Text("Limpieza (aguinaldo):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_LIMPIEZA_AGUI", do_not_clear=False)],

        [sg.Text("Ascensor Mantenimiento:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_ASCENSOR", do_not_clear=False)],
        
        [sg.Text("Mantenimiento (reserva):", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_MANT_RES", do_not_clear=False)],

        [sg.Text("Servicios de Seguridad:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_SEGURIDAD", do_not_clear=False)],

        [sg.Text("Articulos de Librería:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_ART_LIBRERIA", do_not_clear=False)],

        [sg.Text("Fondo de Previsión:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_FONDO", do_not_clear=False)],

        [sg.Text("Seguro R.C. Propiedad Horizontal:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_PROP_HORIZ", do_not_clear=False)],

        [sg.Text("Gastos Bancarios mensuales:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_BANCARIOS", do_not_clear=False)],

        [sg.Text("Seguro Acc. Personales:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_SEGURO_ACC", do_not_clear=False)],

        [sg.Text("Honorarios Administración:", font='Calibri 12 bold', background_color="#3A424F"), sg.Input(key="S_HONORARIOS", do_not_clear=False)],

        # Caja comentarios
        [sg.Text("Comentarios", font='Calibri 12 bold', background_color="#3A424F")],
        [sg.Multiline (size=(90, 3))],

        # Botón
        [sg.Button("RESET", font="Calibri 13 bold", key='-CLEAR-', button_color="#E04C5E"), sg.Button("EXPENSAS", font='Calibri 13 bold')],
        
        
    ]

    # Se incluyen en el layout principal los Tabs:  frame_datos_inquilino / frame_datos_consorcio / frame_impuestos
    layout = [
        
        [sg.TabGroup([
                        [sg.Tab("Datos Inquilino", frame_datos_inquilino, element_justification="right", background_color="#3A424F")],
                        [sg.Tab("Datos Consorcio", frame_datos_consorcio, element_justification="right", background_color="#3A424F")], 
                        [sg.Tab("Impuestos", frame_impuestos, element_justification="right", background_color="#3A424F")],
                        
                    ])
        ]
        
        ]

    window = sg.Window("Inmobiliaria Software", layout, margins=(50,20), element_justification="right")

    today = datetime.datetime.today()
    plazo_1_del = today + datetime.timedelta(days=5)
    plazo_1_al = today + datetime.timedelta(days=30)
    plazo_2_del = today + datetime.timedelta(days=30)
    plazo_2_al = today + datetime.timedelta(days=40)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "EXPENSAS":
            answer=sg.PopupYesNo(f"Registrar expensas de {values['CLIENTE']}?")
            if answer == 'No':
                sg.WIN_CLOSED
            else:
                # Add calculated fields to our dict
                values["SALDO_TOTAL"] = round(float(values['SALDO_ANTERIOR'])) + round(float(values['MES_CORRIENTE']))
                values["VENCIMIENTO_2"] = round(float(values['SALDO_TOTAL'])) + round(float(values['SALDO_TOTAL'])) * round(float(values['RECARGO_2']) / 100, 2)
                values["TODAY"] = today.strftime("%d-%m-%Y")
                values["PLAZO_1_DEL"] = plazo_1_del.strftime("%d-%m-%Y")
                values["PLAZO_1_AL"] = plazo_1_al.strftime("%d-%m-%Y")
                values["PLAZO_2_DEL"] = plazo_2_del.strftime("%d-%m-%Y")
                values["PLAZO_2_AL"] = plazo_2_al.strftime("%d-%m-%Y")

                

                #Render the template, save new word document & inform user
                doc.render(values)
                output_path = Path(__file__).parent / f"{values['CLIENTE']}-expensas-{values['MES']} .docx"
                doc.save(output_path)
                sg.popup("Archivo Registrado", f"El archivo se guardo en la ruta: {output_path}")
                


    window.close()