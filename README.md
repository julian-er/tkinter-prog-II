# Programación II 
## Proyecto Final - Python

### Alcances y requerimientos

El proyecto nace luego de una observación a la falta de una herramienta
para gestionar las expensas de los consorcios de edificios de forma organizada y
estandarizada.
La solución propuesta, consiste en el desarrollo de un software de carácter
empresarial orientado al campo inmobiliario, cuya finalidad es la de facilitar la
gestión y descripción de los datos relativos a las expensas de cada consorcio.
Esto se logrará a través de un sistema que contará con campos definidos y una
interfaz gráfica intuitiva para el usuario dando como resultado la generación de un
documento de fácil lectura para los inquilinos y propietarios de un consorcio, con los
detalles inherentes a las expensas mensuales, y agregando además en una
segunda instancia, su respectivo comprobante de pago.
En cuanto a los requerimientos, el sistema deberá generar un documento listo para
imprimir con la fecha de elaboración, los datos personales pertenecientes a cada
inquilino o propietario, los datos pertenecientes a los gastos de la vivienda
(impuestos), reflejar las deudas de lo meses precedentes (si la hubiere), ajustes por
inflación (en caso de pagar las expensas en más de una cuota), montos totales y
parciales, redondeos de las cifras, datos útiles de contacto de emergencia (plomero,
gasista, cerrajería, mantenimiento ascensor, etc.).
Incluirá los datos bancarios del consorcio para realizar los depósitos
correspondientes y contará también con un campo de comentarios en caso de ser
necesario añadir información extraordinaria. En una segunda instancia, al momento
del pago, el sistema generará el recibo de pago, con la fecha, monto abonado y los
datos del inquilino que efectuó dicho pago.


### Diseño de la Funcionalidad (Explicación de Procesos y secuencias)
El sistema será programado utilizando las librerías TkInter, PySimpleGUI y docxtpl
entre otras.
Como prerrequisito, se realizará separadamente dos plantillas iniciales en formato
de documento word, es decir, ambas con la extensión .docx.
La primera, servirá para generar las expensas con los gastos comunes e impuestos
detallados y la segunda, para generar el recibo de comprobante al momento del
pago, ambas con sus respectivas variables en cuanto a datos personales y montos.
El usuario, mediante la interfaz del sistema, deberá ingresar los datos
correspondientes a las variables (nombre, apellido, edificio, departamento, montos
de los distintos impuestos, etc.) y generar las expensas.
Con la ayuda de la biblioteca de python “docxtpl” estas variables serán
reemplazadas con los datos ingresados por el usuario y generará un documento
nuevo, listo para imprimir o enviar por mail a los inquilinos o propietarios de los
distintos consorcios.
El usuario deberá realizar el mismo proceso de rellenado de campos obteniendo
resultados similares al generar los recibos de pago.

### Interfaz gráfica
Para la interfaz gráfica de usuario (GUI por sus siglas en inglés), se considera
implementar la librería PySimpleGUI (ya que en su base esta utiliza TkInter), tanto
por su versatilidad a la hora de programar este tipo de proyectos, como por su
compatibilidad con los principales sistemas operativos (Windows, macOS y Linux)
Se desarrollará en dos ventanas que separarán el sistema para generar
expensas de aquel que será utilizado para generar un comprobante de pago y cuyos
colores predominantes serán tonos oscuros, siendo esta una medida que ayudará al
usuario a mantener la vista en el sistema por un tiempo prolongado sin generar
fatiga visual como sí lo harían los colores claros o brillantes. Por su parte en los
botones que denotan acciones del usuario se decidió la utilización de un color
similar al rojo para aquellas acciones que pueden ser “peligrosas” para el usuario,
como por ejemplo el borrado de los datos de toda la plantilla y un color de la gama
del azul que se verá utilizado en aquellos botones con acciones mas “amigables”
como por ejemplo la creación final del documento.
Internamente ambas pantallas podrán contener una o más “Tabs” para lograr
una experiencia de usuario simple e intuitiva, siendo la cantidad necesaria para que
el mismo pueda navegar por la aplicación de manera fluida. La cantidad de estas se
verá afectada según datos sean necesarios, ya que si los datos son demasiados se
generaría una pantalla demasiado extensa y tediosa. O si al ofertar dicha aplicación
el usuario, solicitara la división de carga de datos por una agrupación específica.
Un claro ejemplo para esta situación de pestañas puede ser la necesidad de
dividir la carga de datos en “datos inquilino”, “datos consorcio” e “impuestos” para
así visualizar claramente lo que se está ingresando en cada momento.
Al iniciar la aplicación también nos encontraremos con una primera ventana
que nos pedirá seleccionar que es lo que queremos generar constando de un título y
solo dos botones.

#### Plantilla Inicial
Como se indicó anteriormente un prerrequisito claro es la inclusión de
plantillas de la extensión “.docx” las cuales serán utilizadas para finalmente generar
con los datos ingresados nuestras expensas. Es por ello que se realizan
separadamente dos plantillas iniciales.
La primera servirá para generar las expensas detalladas y la segunda, para
generar el recibo de comprobante al momento del pago. Estas, exhiben los detalles
de las expensas del consorcio y los datos personales del inquilino o propietario con
sus respectivas variables, las cuales vendrán reemplazadas a través del sistema.
En ambos casos podemos ver que en las plantillas los datos se ven reflejados
por los nombres de variables que están solo para marcar la posición, es decir, no
significa que estos nombres sean los finales en el modelo desarrollado finalmente. Al
momento de generar estos documentos el mismo sistema se encargará de rellenar
los datos correspondientes
