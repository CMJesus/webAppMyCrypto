from consulta_api import getPU


# Estructura de función

choices=[('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), 
        ('TRX', 'Tron'), ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), ('BCHSV', 'BitcoinSV'), ('USDT', 'StDolar'), ('BSV', 'Bsv'), ('ADA', 'Cardano')]


# Euro no tiene que entrar
def getValorCryptos(dbManager):
    valorSaldoCryptoAcumulado = 0
    
    for choice in choices:
        cryptoCode = choice[0]

        if cryptoCode != "EUR":
            saldoCrypto = getSaldo(dbManager, cryptoCode)

            print(saldoCrypto)

            valorPU = getPU(cryptoCode, "EUR")[1]
            print(valorPU)
            valorSaldoCrypto = valorPU * saldoCrypto

            valorSaldoCryptoAcumulado = valorSaldoCrypto + valorSaldoCryptoAcumulado

    return valorSaldoCryptoAcumulado


def getSaldo(dbManager, cryptoCode):
    return getSumaTo(dbManager, cryptoCode)-getSumaFrom(dbManager, cryptoCode)


def getSumaFrom(dbManager, cryptoCode):
    consulta = """SELECT SUM(Q_desde) as SUMA FROM myCrypto WHERE desde='""" + cryptoCode + """';"""
    queryDataResult = dbManager.consultaSQL(consulta)
    if queryDataResult[0]['SUMA'] == None:
        return 0
    else: 
        return queryDataResult[0]['SUMA']


def getSumaTo(dbManager, cryptoCode):
    consulta = """SELECT SUM(Q_hasta) as SUMA FROM myCrypto WHERE hasta='""" + cryptoCode + """';"""
    queryDataResult = dbManager.consultaSQL(consulta)
    if queryDataResult[0]['SUMA'] == None:
        return 0
    else: 
        return queryDataResult[0]['SUMA']





# def getSaldo(dbManager):
#     return getSumaTo(dbManager)-getSumaFrom(dbManager)

# def getSumaTo(dbManager):
#     consulta = """SELECT SUM(Q_hasta) as SUMA FROM myCrypto WHERE hasta='EUR';"""
#     queryDataResult = dbManager.consultaSQL(consulta)
#     return queryDataResult[0]['SUMA']

# def getSumaFrom(dbManager):
#     consulta = """SELECT SUM(Q_desde) as SUMA FROM myCrypto WHERE desde='EUR';"""
#     queryDataResult = dbManager.consultaSQL(consulta)
#     return queryDataResult[0]['SUMA']


###############

# def getSaldo(dbManager):
#     consulta = """SELECT SUM(Q_hasta) as SUMA FROM myCrypto WHERE hasta='EUR';"""
#     queryDataResult = dbManager.consultaSQL(consulta)

#     return queryDataResult[0]['SUMA']

#complementar con los euros from

# def getInvertido(dbManager):
#     consulta = """SELECT SUM(Q_hasta) as SUMA FROM myCrypto WHERE hasta='EUR';"""
#     queryDataResult = dbManager.consultaSQL(consulta)

#     return queryDataResult[0]['SUMA']

