# ************************************************************
# ------------------- MONTAMOS LA API ------------------------
# ************************************************************

from appRegistro import app
from flask import flash
import requests
import decimal

url = app.config.get("URL_CONSULTA")
apikey = app.config.get("APIKEY_CONSULTA")
header = {"X-CoinAPI-Key": apikey}
#print(apikey)

class APIerror(Exception):
    pass

# FUNCIÓN GET_PU, con argumentos de entrada ("desde" y "hasta").
# Para el caso en que el GET haya sido bien ejecutado = 200 (success).  
# Devuelve como respuesta el valor "rate" resultante de entre las cryptoCode insertadas como parámetros/argumentos. 
def getPU(desde, hasta):
    try:
        answer = requests.get(url.format(desde, hasta), headers = header)
        print(answer.json())

        if answer.status_code == 200:
            rate = answer.json()['rate']
        else: 
            rate = 0
            flash("ERROR EN LA CONSULTA: " + status_code)
            print("ERROR DE STATUS CODE: " + status_code)
    except Exception as e:
        raise APIerror(e)
    return answer.status_code, rate




