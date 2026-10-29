from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'proyecto_integrador'

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('formulario.html')


@app.route('/enviar', methods=['POST'])
def enviar_datos():
    if request.method == 'POST':
  
        nombre = request.form['nombre_usuario']
        correo = request.form['correo_usuario']
        mensaje = request.form['mensaje_usuario']
        
   
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO datos_formulario (nombre, correo, mensaje) VALUES (%s, %s, %s)",
            (nombre, correo, mensaje)
        )
        mysql.connection.commit()
        cur.close()
        
        return "¡Datos guardados con éxito en la Base de Datos!"

if __name__ == '__main__':
    app.run(debug=True)