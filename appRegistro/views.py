from appRegistro import app
from flask import render_template, request, redirect, url_for, flash
from appRegistro.models import DBManager
from appRegistro.forms import MovimientoFormulario
from consulta_api import getPU
from appRegistro.queriesDB import getSaldo, getSumaFrom, getValorCryptos

ruta_basedatos = app.config.get("RUTA_BASE_DATOS")
dbManager = DBManager(ruta_basedatos)

@app.route("/")
def start():
    consulta = """
        SELECT * 
            FROM myCrypto ORDER BY date;
    """
    movimientos = dbManager.consultaSQL(consulta)
    return render_template("index.html", items=movimientos)


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    formulario = MovimientoFormulario()
    if request.method == "POST":
        
        if request.form.get("Enviar"):
            if formulario.validate():
                consulta = """INSERT INTO myCrypto (date, time, desde, Q_desde, hasta, Q_hasta, PU)
                                VALUES (:date, :time, :desde, :Q_desde, :hasta, :Q_hasta, :PU)"""
                
                try:
                    dbManager.ejecutarSQL(consulta, formulario.data)
                except Exception as ex:
                    print("Se ha producido un error de acceso a base de datos.", ex)
                    flash("Se ha producido un error en la base de datos. Consulte con su administrador")
                    print(consulta)
                    return render_template("nuevo_mov.html", form = formulario)

                return redirect(url_for("start"))
            else:
                return render_template("nuevo_mov.html", form = formulario)

            # Validar formulario
            # si la validación es Ok, insertar registro en Tabla y redireccionar a /
            # si la validación no es Ok, devolver formulario y render_template
            # preparar plantilla para gestionar errores

        elif request.form.get("Calcular"):
            value_desde = formulario.desde.data 
            value_hasta = formulario.hasta.data 
            
            print(value_desde, value_hasta)
            
            if value_desde == value_hasta:
                flash("Debe de indicar una moneda distinta")
                return render_template("nuevo_mov.html", form=formulario)
            else:
                status_code, rate = getPU(value_desde, value_hasta)
                
                print(status_code, rate)
                
                formulario.PU.data = rate
                value_PU = rate
                return render_template("nuevo_mov.html", form=formulario, value_PU=rate)
                

# Habilitar botón enviar una vez que se haya hecho el cálculo


    elif request.method == "GET":
        return render_template("nuevo_mov.html", form=formulario)


@app.route("/status", methods=["GET"])
def status():
    saldo = getSaldo(dbManager, "EUR")
    invertido = getSumaFrom(dbManager, "EUR")
    valor = getValorCryptos(dbManager) 

    return render_template("status.html", saldo=saldo, invertido=invertido, valor=valor)





#   """INSERT INTO myCrypto (date, time, desde, Q_desde, hasta, Q_hasta, PU) VALUES (:date, :time, :desde, :Q_desde, :hasta, :Q_hasta, :PU)"""