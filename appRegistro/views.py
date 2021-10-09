from appRegistro import app
from flask import render_template, request
from appRegistro.models import DBManager
from appRegistro.forms import MovimientoFormulario


ruta_basedatos = app.config.get("RUTA_BASE_DATOS")
dbManager = DBManager(ruta_basedatos)


@app.route("/")
def start():
    consulta = """
        SELECT * 
            FROM myCrypto;
    """

    movimientos = dbManager.consultaSQL(consulta)
    return render_template("index.html", items=movimientos)


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    formulario = MovimientoFormulario()

    if request.method == 'GET':
        return render_template("nuevo_mov.html", form=formulario)
    else:
        if formulario.validate():
            consulta = """INSERT INTO movimientos (fecha, concepto, ingreso_gasto, cantidad)
                            VALUES (:fecha, :concepto, :ingreso_gasto, :cantidad)"""

            try:
                dbManager.insertaSQL(consulta, formulario.data)
            except Exception as es:
                print("Se ha producido un error de acceso a base de datos:", e)
                flash("Se ha producido un error en la base de datos. Consulte con su administrador")
                return render_template("nuevo_mov.html", el_formulario=formulario)

            return redirect(url_for("inicio"))
        else:
            return render_template("nuevo_mov.html", form = formulario)

        # Validar formulario
        # si la validación es Ok, insertar registro en Tabla y redireccionar a /
        # si la validación no es Ok, devolver formulario y render_template
        #         preparar plantilla para gestionar errores
