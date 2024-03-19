import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(name, email, phoneNum, credit_interest_label, message):
    # Configuración de los parámetros del correo
    remitente = 'rogafinwebcontacto@gmail.com'
    destinatario = 'rogafinwebcontacto@gmail.com'
    contraseña = 'ghyl pzcb wrdu dqxn'
    servidor_smtp = 'smtp.gmail.com'
    puerto = 587

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Correo de contacto de ' + name

    # Aquí puedes escribir tu HTML
    cuerpo = """
    <html>
    <body style="margin: 0; padding: 0; font-family: sans-serif;">
        <div style="margin: 0 auto; padding: 0;">
            <div style="width: 50%; height: 150px; background-color: #107353; display: flex; justify-content: center; align-items: center;">
                <img style="width: 250px; margin: 0 auto;" src="https://i.ibb.co/pK0j3N2/logoblanco-Photoroom.webp" alt="Logo Rogafin">
            </div>
            <div>
                <h1 style="color: green;"><Mensaje enviado por, {}!</h1>
                <p style="font-size: 1.5rem; color: #3D3B40;"><span style="font-weight: 800;">Nombre:</span> {}</p>
                <p style="font-size: 1.5rem; color: #3D3B40;"><span style="font-weight: 800;">Email:</span> {}</p>
                <p style="font-size: 1.5rem; color: #3D3B40;"><span style="font-weight: 800;">Numero de teléfono:</span> {}</p>
                <p style="font-size: 1.5rem; color: #3D3B40;"><span style="font-weight: 800;">Crédito en el que esta intersado:</span> {}</p>
                <p style="font-size: 1.5rem; color: #3D3B40;"><span style="font-weight: 800;">Mensaje:</span> {}</p>
            </div>
        </div>
    </body>
</html>
    """.format(name, name, email, phoneNum, credit_interest_label, message)

    mensaje.attach(MIMEText(cuerpo, 'html'))  # Aquí cambiamos 'plain' por 'html'

    # Enviar el correo
    try:
        servidor = smtplib.SMTP(servidor_smtp, puerto)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        texto = mensaje.as_string()
        servidor.sendmail(remitente, destinatario, texto)
        servidor.quit()
        print('Correo enviado exitosamente')
    except Exception as e:
        print(f'Error al enviar el correo: {e}')