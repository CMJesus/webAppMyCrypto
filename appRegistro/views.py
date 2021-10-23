from appRegistro import app
from flask import render_template, request, redirect, url_for, flash
from appRegistro.models import DBManager
from appRegistro.forms import MovimientoFormulario
from consulta_api import getPU
from appRegistro.queriesDB import getSaldo, getSumaFrom, getValorCryptos

ruta_basedatos = app.config.get("RUTA_BASE_DATOS")
dbManager = DBManager(ruta_basedatos)

# ************************************************************
# -------------------------VISTAS  (entrada de appRegistro)---
# ************************************************************

# 1) INICIO.--------------------------------------------------
@app.route("/")
def start():
    consulta = """
        SELECT * 
            FROM myCrypto ORDER BY date;
    """
    movimientos = dbManager.consultaSQL(consulta)
    return render_template("index.html", items=movimientos, disableInicio=True)

# 2) NUEVA TRANSACCIÓN.---------------------------------------
@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    formulario = MovimientoFormulario()
    if request.method == "POST":
        
        # Enviar:---------------------------------------------
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
                    return render_template("nuevo_mov.html", form = formulario, disableNuevo=True)
                return redirect(url_for("start"))
            else:
                return render_template("nuevo_mov.html", form = formulario, disableNuevo=True)
        
        # Calcular:------------------------------------------- 
        # Función que calcula qué rate hay entre las distintas monedas "desde" y "hasta" (formulario).
        elif request.form.get("Calcular"):
            value_desde = formulario.desde.data 
            value_hasta = formulario.hasta.data
            value_Q_desde = formulario.Q_desde.data

            if value_desde == "EUR":
                saldo = value_Q_desde
            else:
                saldo = getSaldo(dbManager, value_desde)

            if saldo >= value_Q_desde:
                print(value_desde, value_hasta)
                
                if value_desde == value_hasta:
                    flash("Las monedas no pueden ser iguales")
                    return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)
                else:
                    status_code, rate = getPU(value_desde, value_hasta)
                    print(status_code, rate)
                    
                    formulario.PU.data = rate
                    value_PU = rate
                    return render_template("nuevo_mov.html", form=formulario, disableNuevo=True, value_PU=rate)
            else:
                flash("No hay saldo disponible para realizar la transacción. Su saldo disponible es: " + str(saldo))
                return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)

    elif request.method == "GET":
        return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)

# 3) STATUS PORTFOLIO.--------------------------------------
@app.route("/status", methods=["GET"])
def status():
    saldo = getSaldo(dbManager, "EUR")
    invertido = getSumaFrom(dbManager, "EUR")
    valor = getValorCryptos(dbManager)

    return render_template("status.html", disablePortfolio=True, saldo=saldo, invertido=invertido, valor=valor)


