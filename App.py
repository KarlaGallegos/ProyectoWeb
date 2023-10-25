from flask import Flask, render_template, request, url_for, flash, redirect, send_file, make_response,jsonify
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from io import BytesIO
from reportlab.lib.utils import ImageReader
import pymysql
import tempfile
import model.package_model.Database as Database
import model.package_model.Asunto as Asunto
import model.package_model.Municipio as Municipio
import model.package_model.Nivel_Educativo as Nivel
import model.package_model.Alumno as Alumno
import model.package_model.Representante as Representante
import model.package_model.Ticket_Turno as Ticket

app = Flask(__name__, template_folder='templates', root_path=r'C:\\Users\\Karla Gallegos\\Documents\\DesarrolloWeb\\ProyectoWeb')
app.config['SECRET_KEY'] = 'j\x86\x14\xcc:\x99\xb3\x91\xf8/Bv\r\xaa"\xf1\x8a\xfa(A\xa1\xe2\x85\xd6'

db = pymysql.connect(host='localhost', user='root', password='041002', db='TICKET_TURNODB')
cursor = db.cursor()

def get_next_numero_turno(id_municipio):
    conexion = Database.Database()
    with conexion.cursor as cursor:
        cursor.execute("SELECT MAX(NUMERO_TURNO) FROM TICKET_TURNO WHERE ID_MUNICIPIO = %s", id_municipio)
        max_numero_turno = cursor.fetchone()[0]
        if max_numero_turno is not None:
            return max_numero_turno + 1
        else:
            return 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ticket")
def add_ticket():
    obj_asunto = Asunto.Asunto()
    obj_municipio = Municipio.Municipio()
    obj_nivel = Nivel.Nivel_Educativo()
    lista_asunto = obj_asunto.obtener_asuntos()
    lista_municipio = obj_municipio.obtener_municipios()
    lista_nivel = obj_nivel.obtener_niveles()
    return render_template('ticket_turno.html', lista_asunto=lista_asunto,lista_municipio=lista_municipio,lista_nivel=lista_nivel)

@app.route("/ticket-turno", methods=['POST'])
def ticket_turno():
    _nombre_representante = request.form['representante']
    _curp_alumno = request.form['curp']
    _nombre_alumno = request.form['nombre']
    _paterno = request.form['paterno']
    _materno = request.form['materno']
    _telefono = request.form['telefono']
    _celular = request.form['celular']
    _correo = request.form['correo']
    _id_asunto = request.form['asunto']
    _id_nivel = request.form['nivel']
    _id_municipio = request.form['municipio']
    _id_estatus = 1
    _id_representante = 0
    
    next_numero_turno = get_next_numero_turno(_id_municipio)
    _numero_turno = next_numero_turno

    obj_alu = Alumno.Alumno(_curp_alumno, _nombre_alumno, _paterno, _materno, _id_nivel)
    obj_alu.insertar_alumno(obj_alu)
    obj_rep = Representante.Representante(_id_representante, _nombre_representante, _celular, _telefono, _correo)
    obj_rep.insertar_representante(obj_rep)
    # Insert the ticket into Ticket_Turno table
    obj_tic = Ticket.Ticket_Turno(_id_municipio, next_numero_turno, _nombre_representante, _curp_alumno, _id_asunto, _id_estatus)
    obj_tic.insertar_ticket(obj_tic)
    
    

    # Crear la información para el código QR
    qr_data = f"CURP: {_curp_alumno}, Numero_Turno: {_id_municipio} - {_numero_turno}"
    
    # Crear un objeto QRCode y generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar el código QR en un archivo temporal
    qr_img_path = tempfile.mktemp(suffix='.png')
    qr_img.save(qr_img_path)

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # Calculate the center of the page
    center_x = letter[0] / 2
    center_y = letter[1] / 2

    # Agregar los atributos del ticket
    ticket_info = f"""Información del Ticket:
    Nombre del Representante: {_nombre_representante}
    CURP del Alumno: {_curp_alumno}
    Nombre del Alumno: {_nombre_alumno}
    Paterno: {_materno}
    Materno: {_paterno}
    Asunto: {_id_asunto}
    """
    
    text_lines = ticket_info.split('\n')
    text_x = center_x
    text_y = center_y + 50  # Adjust as needed

    c.setFont("Helvetica", 12)  # Set the font and font size

    for line in text_lines:
        c.drawCentredString(text_x, text_y, line)
        text_y -= 20  # Adjust the line spacing as needed

    # Agregar el código QR al PDF
    qr_x = center_x - 100  # Ajusta la posición X del código QR
    qr_y = center_y - 200  # Ajusta la posición Y del código QR
    qr_width = 100
    qr_height = 100
    
    img = ImageReader(qr_img_path)
    c.drawImage(img, qr_x, qr_y, width=qr_width, height=qr_height)

    # Save the PDF and send it as a downloadable file
    c.showPage()
    c.save()

    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=ticket_{_numero_turno}.pdf'

    flash(f"Ticket registrado exitosamente con número de turno: ", "success")

    return response

@app.route('/lista_representantes')
def lista_representantes():
    # Recupera los representantes de la base de datos
    cursor.execute("SELECT * FROM representante")
    representantes = cursor.fetchall()
    return render_template('representante.html', lista_representantes=representantes)

@app.route('/lista_alumnos')
def lista_alumnos():
    cursor.execute("SELECT * FROM ALUMNO")
    alumnos = cursor.fetchall()
    return render_template('alumno.html', lista_alumnos=alumnos)

@app.route('/lista_tickets')
def lista_tickets():
    cursor.execute("SELECT * FROM TICKET_TURNO")
    tickets = cursor.fetchall()
    return render_template('lista_ticket.html', lista_tickets=tickets)


# Ruta para insertar un representante
@app.route('/insertar_representante', methods=['GET', 'POST'])
def insertar_representante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        celular = request.form['celular']
        telefono = request.form['telefono']
        email = request.form['email']
        representante = Representante.Representante(None, nombre, celular, telefono, email)
        representante.insertar_representante(representante)
        return redirect('/')
    return render_template('insertar_representante.html')

# Ruta para actualizar un representante
@app.route('/actualizar_representante', methods=['GET', 'POST'])
def actualizar_representante():
    if request.method == 'POST':
        id = request.form['id']
        representante = Representante.Representante.obtener_representante_por_id(id)
        if representante is not None:
            nombre = request.form['nombre']
            celular = request.form['celular']
            telefono = request.form['telefono']
            email = request.form['email']
            representante.nombre = nombre
            representante.celular = celular
            representante.telefono = telefono
            representante.email = email
            Representante.actualizar_representante(representante)
            return redirect('/')
        else:
            error_message = "Representante no encontrado."
            return render_template('actualizar_representante.html', error_message=error_message)
    return render_template('actualizar_representante.html')

@app.route('/eliminar_representante', methods=['POST'])
def eliminar_representante():
    if request.method == 'POST':
        representante_id = request.form['representante_id']
        
        # Verifica si el representante con el ID proporcionado existe en la base de datos
        cursor.execute("SELECT * FROM representante WHERE id_representante = %s", (representante_id,))
        representante = cursor.fetchone()

        if representante is not None:
            # Si el representante existe, procede a eliminarlo
            cursor.execute("DELETE FROM representante WHERE id = %s", (representante_id,))
            db.commit()  # Guarda los cambios en la base de datos
            flash(f"Representante con ID {representante_id} ha sido eliminado exitosamente.", "success")
        else:
            flash(f"El representante con ID {representante_id} no existe.", "error")

        return redirect('/lista_representantes')  # Redirige a la lista de representantes

    return render_template('eliminar_representante.html')

@app.route('/insertar_alumno', methods=['GET', 'POST'])
def insertar_alumno():
    if request.method == 'POST':
        curp = request.form['curp']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        id_nivel = request.form['id_nivel']
        alumno = Alumno.Alumno(curp, nombre, paterno, materno, id_nivel)
        alumno.insertar_alumno(alumno)
        return redirect('/insertar_alumno')
    return render_template('insertar_alumno.html')

@app.route('/insertar_ticket', methods=['GET', 'POST'])
def insertar_ticket():
    if request.method == 'POST':
        id_municipio = request.form['id_municipio']
        numero_turno = get_next_numero_turno
        nombre = request.form['nombre_representante']
        curp = request.form['curp_alumno']
        id_asunto = request.form['id_asunto']
        id_estatus = request.form['id_estatus']
        ticket = Ticket.Ticket_Turno(id_municipio,numero_turno, nombre, curp, id_asunto, id_estatus)
        ticket.insertar_ticket(ticket)
        return redirect('/insertar_ticket')
    return render_template('insertar_ticket.html')

if __name__ == "__main__":
    app.run(debug=True)
