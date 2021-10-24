# ************************************************************
# ------------------- MONTAMOS LA API ------------------------
# ************************************************************

from appRegistro import app
import requests
import decimal

url = app.config.get("URL_CONSULTA")
apikey = app.config.get("APIKEY_CONSULTA")
header = {"X-CoinAPI-Key": apikey}
#print(apikey)

# FUNCIÓN GET_PU, con argumentos de entrada ("desde" y "hasta").
# Para el caso en que el GET haya sido bien ejecutado = 200 (success).  
# Devuelve como respuesta el valor "rate" resultante de entre las cryptoCode insertadas como parámetros/argumentos. 
def getPU(desde, hasta):
    answer = requests.get(url.format(desde, hasta), headers = header)
    print(answer.json())

    if answer.status_code == 200:
        rate = answer.json()['rate']
    # elif answer.status_code != 200:
    #     print("ERROR DE STATUS CODE: " + status_code)
    # Me da un status code 500 (aunque no me sale siempre): pero la respuesta es: 
    # {'error': "You requested specific single item that we don't have at this moment."}.
    # Es la moneda Bsv" > REVISAR.    
    else:
        rate = 0
    return answer.status_code, rate




