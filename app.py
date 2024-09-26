from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Conexión a SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=LAPTOP-L5BTHTKJ;'
                      'DATABASE=DB_ahora_si_PC02;'
                      'UID=sa;'
                      'PWD=845623197')
cursor = conn.cursor()

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    Identificacion = request.form['identificacion']
    Titulo = request.form['titulo']
    Profesor = request.form['profesor']
    Descripcion = request.form['descripcion']

    cursor.execute("INSERT INTO Usuariosssssssssssssss (Titulo, Profesor, Descripcion) VALUES (?, ?, ?)", (Titulo, Profesor, Descripcion))
    conn.commit()
    return 'Datos insertados correctamente.'

if __name__ == '__main__':
    app.run(debug=True)
