import sqlite3
from appRegistro import app 
# ************************************************************
# -----------------Funciones Base de Datos--------------------
# ************************************************************

class DBerror(Exception):
    pass

# CLASE DBManager.
class DBManager():
    def __init__(self, ruta_basedatos):
        self.ruta_basedatos = ruta_basedatos

    # MÉTODOS DE LA CLASE:
    
    # FUNCIÓN CONSULTA_SQL:
    def consultaSQL(self, consulta, params = []):
        try:
            conex = sqlite3.connect(self.ruta_basedatos)
            cur = conex.cursor()
            cur.execute(consulta, params)
            # Filas.
            keys = []
            for item in cur.description:
                keys.append(item[0])
            # Columnas.
            registros = []
            for registro in cur.fetchall():
                ix_clave = 0
                d = {}
                for columna in keys:
                    d[columna] = registro[ix_clave]
                    ix_clave += 1
                registros.append(d)
            conex.close()

        except sqlite3.Error as e:
            raise DBerror(e)

        return registros
        

    # FUNCIÓN: EJECUTAR_SQL: 
    # Proceso: "INSERT" (CRUD), desde el "views".
    def ejecutarSQL(self, consulta, params):
        try:
            conex = sqlite3.connect(self.ruta_basedatos)
            cur = conex.cursor()
            claves = params.keys()

            cur.execute(consulta, params)
            conex.commit()
            conex.close()
        except sqlite3.Error as e:
            raise DBerror(e)