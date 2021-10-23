from flask import flash
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, RadioField, SubmitField, SelectField, FloatField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from appRegistro.models import DBManager
import datetime
from appRegistro import app
from appRegistro.queriesDB import getSaldo

# Variable Global "choices".
choices=[('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), 
        ('TRX', 'Tron'), ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), ('BCHSV', 'BitcoinSV'), ('USDT', 'StDolar'), ('BSV', 'Bsv'), ('ADA', 'Cardano')]

# FUNCIÓN: getChoicesDesde.
# Proceso: selecciona las monedas que disponen de crédito:
def getChoicesDesde(dbManager):
    # Euro constante.
    stockChoices=[('EUR', 'Euro')]
    # Este bucle iterará en la lista de tuplas "choices".
    for choice in choices:
        if choice[0] != "EUR":
            # Llamamos a la función getSaldo:
            saldoCrypto = getSaldo(dbManager, choice[0])
            if saldoCrypto > 0:
                stockChoices.append(choice)        
    return stockChoices

# CLASE [*] MovimientoFormulario: 
# Objeto que contiene distintos campos del formulario:
class MovimientoFormulario(FlaskForm):
    ruta_basedatos = app.config.get("RUTA_BASE_DATOS")
    dbManager = DBManager(ruta_basedatos)
    id = HiddenField()
    
    def date_validate(formulario, campo):
        hoy = datetime.date.today()
        if campo.data > hoy:
            flash("La fecha no puede ser posterior a hoy")
            raise ValidationError("La fecha no puede ser posterior a hoy")

    date = DateField("date", validators=[DataRequired(message="Debe de introducir una fecha"), date_validate])
    time = StringField("time", validators=[DataRequired(message="Debe de informar sobre la hora")])
    desde = SelectField("desde", choices=getChoicesDesde(dbManager))
    Q_desde = FloatField("Q_desde", validators=[DataRequired(message="Debe de informar una cantidad")])
    hasta = SelectField("hasta",  choices=choices, validators=[DataRequired(message="Debe de informar la moneda que desea comprar"), Length(max=10)])
    Q_hasta = FloatField("Q_hasta")
    PU = FloatField("PU")


