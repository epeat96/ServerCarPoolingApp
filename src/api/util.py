#!/opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3
from flask import Flask
from flask import request
from functools import wraps

UCAR_API_AUTH_TOKEN = 'JbslEJwMnd7fcfrtqcyT_O4MgTWQ1bau1XtdGhWGXw'
UCAR_API_USER_ID = 'yNPnZACTchuDwdHag'

def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        if request.headers.has_key('X-Auth-Token') and request.headers.has_key('X-User-Id'):
            token = request.headers.get('X-Auth-Token')
            user = request.headers.get('X-User-Id')
            if user in UCAR_API_USER_ID and token in UCAR_API_AUTH_TOKEN:
                return func(*args, **kwargs)
        return {"status":"error","message":"You must be logged in to do this."}
    return check_token

def content_type_json(func):
    @wraps(func)
    def check(*args, **kwargs):
        if request.is_json:
            return func(*args, **kwargs)
        return {"status": "error","message":"Content-Type: application/json"}
    return check

def ucar_sendemail(to, message):
    from smtplib import SMTP
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = 'so2tphids2018@gmail.com'
    msg['To'] = to
    msg['Subject'] = "ucar: recuperar cuenta"
    msg.attach(MIMEText(message, 'plain'))

    server = SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(msg['From'], 'ny4Rla7h0t3P')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def update_user_conn(*user_id):
    from datetime import datetime
    from orm.model.ucar.persona import Persona

    for id in user_id:
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        Persona.update(conexion = now).where(Persona.id == id).execute()

