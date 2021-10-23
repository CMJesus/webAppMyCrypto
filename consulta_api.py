# ************************************************************
# ------------------- MONTAMOS LA API ------------------------
# ************************************************************

# ------------------------------------------------------------
# Importamos la librería "requests" (tras haberla instalado).
# ------------------- pip install requests ------------------
# ------------------------------------------------------------
import requests
import decimal
# ------------------------------------------------------------
# DIRECCIÓN: a donde dirigiremos nuestro request.
# ------------------------------------------------------------
# WEB DE CONSULTA:
# https://rest.coinapi.io/v1/exchangerate/BTC/EUR?
# apikey=FB9EC041-B572-48B2-B6C1-DCBB24B102C2
# ------------------------------------------------------------
# API Key: FB9EC041-B572-48B2-B6C1-DCBB24B102C2
# url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"
# ------------------------------------------------------------

# url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"
# apikey = "FB9EC041-B572-48B2-B6C1-DCBB24B102C2"

# ------------------------------------------------------------
# PREPARACIÓN de los datos para hacer la petición:
# ------------------------------------------------------------
# header = {"X-CoinAPI-Key": apikey}

# ------------------------------------------------------------
# PETICIÓN Y RESPUESTA # requests.+verbo.
# ------------------------------------------------------------
# La petición irá al servidor para ser ejecutada.
# La respuesta será instrumentada a través del .GET
# ------------------------------------------------------------
# answer = requests.get(url, headers = header)

# ------------------------------------------------------------
# Hay que atender a los códigos de respuesta
# ------------------------------------------------------------

# ------------------------------------------------------------
# if answer == 200:
# print(answer.status_code)
# print(answer.text)
# api_data = answer.json()
# print(api_data['rate'])
# print(answer.json()['rate'])

# ------------------------------------------------------------
# La respuesta aquí será tipo diccionario por virtud del .json
# Del .json podemos coger el campo deseado, "rate".

# ************************************************************
# -------------------MONTAMOS EL BUCLE -----------------------
# ************************************************************

url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"
#apikey = "FB9EC041-B572-48B2-B6C1-DCBB24B102C2"#
apikey = "132342DF-03FF-4FE2-A319-ACACF95AE59F"
header = {"X-CoinAPI-Key": apikey}

# Función "getPu", con argumentos de entrada "desde" y "hasta".
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
    # {'error': "You requested specific single item that we don't have at this moment."}    
    else:
        rate = 0
    return answer.status_code, rate

# def consultaAPI():
#     askMore = 's'
#     while askMore == 's':
#         askCoin = input("Divisa de origen: ")
#         answerCoin = input("Divisa de destino: ")
#         answer = requests.get(url.format(askCoin, answerCoin), headers = header)

#         if answer.status_code == 200:
#             print(answer.json()['rate'])
#         else:
#             print(answer.status_code)
#         askMore = input("Desea seguir su consulta? (S/N)").lower()


