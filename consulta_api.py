# ************************************************************
# ------------------- MONTAMOS LA API ------------------------
# ************************************************************

# ------------------------------------------------------------
# Importamos la librería "requests" (tras haberla instalado).
# ------------------- pip install requests ------------------
# ------------------------------------------------------------
import requests

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

url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"
apikey = "FB9EC041-B572-48B2-B6C1-DCBB24B102C2"

# ------------------------------------------------------------
# PREPARACIÓN de los datos para hacer la petición:
# ------------------------------------------------------------
header = {"X-CoinAPI-Key": apikey}

# ------------------------------------------------------------
# PETICIÓN Y RESPUESTA # requests.+verbo.
# ------------------------------------------------------------
# La petición irá al servidor para ser ejecutada.
# La respuesta será instrumentada a través del .GET
# ------------------------------------------------------------
answer = requests.get(url, headers = header)

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

# ------------------------------------------------------------

# PENDIENTE:
# Tengo que validar errores en los status_code, para cuando 
# consulte y haya un error de código, dependiendo del tipo 
# de error, que me muestre un mensaje.


# ************************************************************
# -------------------MONTAMOS EL BUCLE -----------------------
# ************************************************************

askMore = 's'
while askMore == 's':
    askCoin = input("Divisa de origen: ")
    answerCoin = input("Divisa de destino: ")
    answer = requests.get(url.format(askCoin, answerCoin), headers = header)

    if answer.status_code == 200:
        # Códigos de respuesta de HTTP, respuestas informativas, revisar
        print(answer.json()['rate'])
    else:
        print(answer.status_code)
        print(answer.json())

    askMore = input("Desea seguir su consulta? (S/N)").lower()