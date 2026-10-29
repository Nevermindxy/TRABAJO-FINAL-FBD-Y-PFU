# Proyecto Integrador - Formulario Web, mysql y python

## Integrantes
* **ALVAREZ LIMACHI HAROLD YASMANI**
* **CABA MURILLO YASSER RODRIGO**
* **FERNANDEZ ITUSACA IGNACIO**
* **GARCIA BURGOA EMILIO WALTER**

## Que se uso
* **Backend:** Python con la libreria Flask
* **Base de Datos:** MySQL en DBeaver con el uso de XAMPP
* **Frontend:** html

##  Estructura 
* `app.py`: Servidor backend en python para estructurar
* `schema.sql`: Script SQL
* `templates/formulario.html`: Archivo de interfaz de usuario para la captura de datos.



###  Ejecutar la Aplicación y problemas que vimos dentro del proceso de la elaboracion
Para ejecutarlo, lo hicimos desde la terminal de visual poniendo python.py e ingresamos a `http://127.0.0.1:5000` para interactuar con el formulario. Tambien dentro de los problemas estaba las librerias que al descargarlo desde terminal generaba un problema por lo que investigando vimos que es mejor usar py -m pip install flask flask-mysqldb ya que tenia otras versiones de python y no detectaba la libreria, al igual vimos que es mas seguro usar el py -m ya que lo hace directamente desde el lanzador de python de la IDE Visual Studio

Nota adicional: Tambien que para hacer uso del templates habia un error al identificar ese archivo, asi que investigando se puso el archivo formularios.html dentro de la carpeta templates para que asi lo reconociera, siendo mas practica ya que se usa las funciones de la libreta

