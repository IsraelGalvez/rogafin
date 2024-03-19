import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(name, email, message):
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
    cuerpo = message
    mensaje.attach(MIMEText(cuerpo, 'plain'))

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