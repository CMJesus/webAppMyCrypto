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

# ------------------------------------------------------------

# PENDIENTE:
# Tengo que validar errores en los status_code, para cuando 
# consulte y haya un error de código, dependiendo del tipo 
# de error, que me muestre un mensaje.


# ************************************************************
# -------------------MONTAMOS EL BUCLE -----------------------
# ************************************************************

url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"
apikey = "FB9EC041-B572-48B2-B6C1-DCBB24B102C2"
header = {"X-CoinAPI-Key": apikey}

# Esta función parte de dos monedas y devuelve el codigo de la respuesta y el valor del rate en caso de que la respuesta haya sido success = 200, si no, devuelve 0 como segundo valor
def getPU(desde, hasta):
    answer = requests.get(url.format(desde, hasta), headers = header)
    
    #print(answer.json())

    if answer.status_code == 200:
        return answer.status_code, answer.json()['rate']
    else:
        return  answer.status_code, 0
  


def consultaAPI():
    askMore = 's'
    while askMore == 's':
        askCoin = input("Divisa de origen: ")
        answerCoin = input("Divisa de destino: ")
        answer = requests.get(url.format(askCoin, answerCoin), headers = header)

        if answer.status_code == 200:
            print(answer.json()['rate'])
        else:
            print(answer.status_code)


        askMore = input("Desea seguir su consulta? (S/N)").lower()

# PENDIENTE:
# Tengo que validar errores en los status_code, para cuando 
# consulte y haya un error de código, dependiendo del tipo 
# de error, que me muestre un mensaje.
# Hacer función Consulta que conectará con la transacción
# Conectar el valor con el formulario, para referenciarlo y guardarlo