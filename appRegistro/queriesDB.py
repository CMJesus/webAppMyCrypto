from consulta_api import getPU

# ************************************************************
# -----------Funciones del DBManager (Clase/Objeto)-----------
# ************************************************************
# 
# LISTA DE MONEDAS PARA LOS CAMPOS DEL FORMULARIO Y FUNCIONES:
choices=[('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), 
        ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), 
        ('TRX', 'Tron'), ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), 
        ('BCH', 'Bitcoin Cash'), ('USDT', 'StDolar'), ('BCHSV', 
        'Bitcoin SV'), ('ADA', 'Cardano')
        ]

# FUNCIÓN GETVALOR,llamada por el  bucle FOR "choices"; 
def getValorCryptos(dbManager):
    valorSaldoCryptoAcumulado = 0
    # para cada moneda en monedas, siendo cryptoCode el unit economic.    
    for choice in choices:
        cryptoCode = choice[0]
        
        if cryptoCode != "EUR":
            # Llamo a getSaldo
            saldoCrypto = getSaldo(dbManager, cryptoCode)
            print(saldoCrypto)
            # Llamo a valorPU
            valorPU = getPU(cryptoCode, "EUR")[1]
            print(valorPU)
            valorSaldoCrypto = valorPU * saldoCrypto
            valorSaldoCryptoAcumulado = valorSaldoCrypto + valorSaldoCryptoAcumulado
    return valorSaldoCryptoAcumulado

# FUNCIÓN GETSALDO; argumentadas por las funciones getSumaFrom y getSumaTo.
    # Proceso: obtener el saldo de una "cryptoCode". 
    # Se inicia por la llamada de la Función "getChoicesDesde", y por la "vista" "status".
    # Retorna: saldo de una cryptoCode en la BD. 
def getSaldo(dbManager, cryptoCode):
    return getSumaTo(dbManager, cryptoCode)-getSumaFrom(dbManager, cryptoCode)

# 1) FUNCIÓN GET SUMA FROM:
def getSumaFrom(dbManager, cryptoCode):
    consulta = """SELECT 
    SUM(Q_desde) as SUMA 
    FROM myCrypto WHERE desde='""" + cryptoCode + """';
    """
    queryDataResult = dbManager.consultaSQL(consulta)
    if queryDataResult[0]['SUMA'] == None:
        return 0
    else: 
        return queryDataResult[0]['SUMA']

# 2) FUNCIÓN GET SUMA TO:
def getSumaTo(dbManager, cryptoCode):
    consulta = """SELECT 
    SUM(Q_hasta) as SUMA 
    FROM myCrypto WHERE hasta='""" + cryptoCode + """';
    """
    queryDataResult = dbManager.consultaSQL(consulta)
    if queryDataResult[0]['SUMA'] == None:
        return 0
    else: 
        return queryDataResult[0]['SUMA']