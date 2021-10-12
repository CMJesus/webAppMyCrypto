import sqlite3


class DBManager():
    def __init__(self, ruta_basedatos):
        self.ruta_basedatos = ruta_basedatos

    def consultaSQL(self, consulta, params = []):
        conex = sqlite3.connect(self.ruta_basedatos)
        cur = conex.cursor()
        cur.execute(consulta, params)
        
        keys = []
        for item in cur.description:
            keys.append(item[0])

        registros = []
        for registro in cur.fetchall():
            ix_clave = 0
            d = {}
            for columna in keys:
                d[columna] = registro[ix_clave]
                ix_clave += 1
            registros.append(d)
        conex.close()
        return registros

    def ejecutarSQL(self, consulta, params):
        conex = sqlite3.connect(self.ruta_basedatos)

        cur = conex.cursor()
        claves = params.keys()

        cur.execute(consulta, params)
        conex.commit()
        conex.close()

# Aquí hay que crear las funciones para la tercera plantilla