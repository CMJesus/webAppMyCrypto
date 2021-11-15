from appRegistro import app
from flask import render_template, request, redirect, url_for, flash
from appRegistro.models import DBManager, DBerror
from appRegistro.forms import MovimientoFormulario
from consulta_api import getPU, APIerror
from appRegistro.queriesDB import getSaldo, getSumaFrom, getValorCryptos

ruta_basedatos = app.config.get("RUTA_BASE_DATOS")
dbManager = DBManager(ruta_basedatos)

# ************************************************************
# ----------- VISTAS (entrada de appRegistro)-----------------
# ************************************************************

# 1) FUNCIÓN INICIO:
@app.route("/")
def start():
    try:
        consulta = """
            SELECT * 
                FROM myCrypto ORDER BY date;
        """
        movimientos = dbManager.consultaSQL(consulta)
        return render_template("index.html", items=movimientos, disableInicio=True)
    except DBerror as e:
        flash ("Se ha producido un error de acceso a la base de datos,  " + str(e))
        print(e)
        return render_template("index.html", disableInicio=True)

# 2) FUNCIÓN NUEVA TRANSACCIÓN:
@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    try:
        formulario = MovimientoFormulario()
        formulario.desde.choices = formulario.getChoicesDesde()
    except DBerror as e:
        flash("No hay información disponible. Error en la consulta de acceso a la base de datos,  " + str(e))

    if request.method == "POST":
        # FUNCIÓN ENVIAR (método POST):
        if request.form.get("Enviar"):
            if formulario.validate():
                if formulario.hasta_noChange.data != formulario.hasta.data or formulario.desde_noChange.data != formulario.desde.data:
                    print("Error, los campos de seleción no deben de modificarse una vez pulsado el botón calcular. Vuelva a calcular la transacción")
                    flash("Error, los campos de seleción no deben de modificarse una vez pulsado el botón calcular. Vuelva a calcular la transacción")
                    return render_template("nuevo_mov.html", form = formulario, disableNuevo=True)
                else:
                    flash("FORMULARIO VALIDADO")
                    consulta = """INSERT 
                    INTO myCrypto (date, time, desde, Q_desde, hasta, Q_hasta, PU)
                    VALUES (:date, :time, :desde, :Q_desde, :hasta, :Q_hasta, :PU)
                    """
                    try:
                        dbManager.ejecutarSQL(consulta, formulario.data)
                    except DBerror as e:
                        print("Error de acceso a base de datos.", e)
                        flash("Error en la base de datos, consulte con su administrador. ")
                        #print(consulta)
                        return render_template("nuevo_mov.html", form = formulario, disableNuevo=True)
                    return redirect(url_for("start"))
            else:
                flash("Debe de completar todos los campos del formulario.")
                return render_template("nuevo_mov.html", form = formulario, disableNuevo=True)
        
        # FUNCIÓN CALCULAR:
        # Proceso: calcula el "rate" existente entre las monedas "desde" y "hasta" (formulario).
        # Resultado: valor a través de "rate".
        elif request.form.get("Calcular"):
            value_desde = formulario.desde.data 
            formulario.desde_noChange.data = formulario.desde.data
            value_hasta = formulario.hasta.data
            formulario.hasta_noChange.data = formulario.hasta.data
            value_Q_desde = formulario.Q_desde.data

            if value_desde == "EUR":
                saldo = value_Q_desde
            else:
                try:
                    saldo = getSaldo(dbManager, value_desde)
                except DBerror() as e:
                    flash("Error calculando saldo, consulte con su administrador,  " + str(e))

            if saldo >= value_Q_desde:
                print(value_desde, value_hasta)
                
                if value_desde == value_hasta:
                    
                    # Si meto cantidades a mano en los dos ultimos, me deja meter de euro a euro
                    
                    flash("Las monedas no pueden ser iguales")
                    return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)
                else:
                    try:
                        status_code, rate = getPU(value_desde, value_hasta)
                        print(status_code, rate)
                    except APIerror as e:
                        print("Se ha producido un error en la consulta a la API.", e)
                        flash ("Se ha producido un error en la consulta a la API.")
                        return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)

                    if status_code != 200:
                        flash("Ha habido un problema de conexión con el servidor al realizar la consulta -API-.")
                        return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)
                    else:
                        return render_template("nuevo_mov.html", form=formulario, disableNuevo=True, value_PU=rate)
                    
            else:
                flash("No hay saldo disponible para realizar la transacción. Su saldo disponible es: " + str(saldo))
                return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)
                        
    elif request.method == "GET":
        return render_template("nuevo_mov.html", form=formulario, disableNuevo=True)

# 3) FUNCIÓN STATUS PORTFOLIO:
# Proceso: procesar las cantidades recibidas por las funciones llamadas.
# Resultado: cantidades.
@app.route("/status", methods=["GET"])
def status():
    try:
        saldo = getSaldo(dbManager, "EUR")
        invertido = getSumaFrom(dbManager, "EUR")
        valor = getValorCryptos(dbManager)
        return render_template("status.html", disablePortfolio=True, saldo=saldo, invertido=invertido, valor=valor)
    except DBerror as e:
        print("Error de acceso a base de datos.", e)
        flash("Error calculando saldo, consulte con su administrador,  " + str(e))
        return render_template("status.html", saldo=0, invertido=0, valor=0, disablePortfolio=True)
    except APIerror as e:
        print("Error en la consulta API.", e)
        flash ("Se ha producido un error en la consulta a la API.")
        return render_template("status.html", saldo=0, invertido=0, valor=0, disablePortfolio=True)
        
