import sqlite3

# CLASE [*] DBManager.
class DBManager():
    def __init__(self, ruta_basedatos):
        self.ruta_basedatos = ruta_basedatos

    # MÉTODOS [*]:
    # FUNCIÓN: ConsultaSQL:
    def consultaSQL(self, consulta, params = []):
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
        
        return registros

    # FUNCIÓN: EjecutarSQL: 
    # Proceso: "INSERT" (CRUD), desde el "views".
    def ejecutarSQL(self, consulta, params):
        conex = sqlite3.connect(self.ruta_basedatos)
        cur = conex.cursor()
        claves = params.keys()

        cur.execute(consulta, params)
        conex.commit()
        conex.close()