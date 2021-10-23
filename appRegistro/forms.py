from flask import flash
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, RadioField, SubmitField, SelectField, FloatField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from appRegistro.models import DBManager
import datetime
from appRegistro import app
from appRegistro.queriesDB import getSaldo

# VARIABLE GLOBAL: "choices".
choices=[
    ('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), 
    ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), ('TRX', 'Tron'), 
    ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), ('BCHSV', 'BitcoinSV'), ('USDT', 
    'StDolar'), ('BSV', 'Bsv'), ('ADA', 'Cardano')
        ]

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
    # FUNCIÓN VALIDAR FECHA:
    # Proceso: validar la fecha, comparándola a fecha de hoy; no puede ser mayor.
    def date_validate(formulario, campo):
        hoy = datetime.date.today()
        if campo.data > hoy:
            flash("La fecha no puede ser posterior a hoy")
            raise ValidationError("La fecha no puede ser posterior a hoy")
    
    # FORMULARIO:
    # Campo FECHA:
    date = DateField("date", validators=[DataRequired(message="Debe de introducir una fecha"), date_validate])
    # Campo TIEMPO:
    time = StringField("time", validators=[DataRequired(message="Debe de informar sobre la hora")])
    # Campo MONEDA_DESDE:
    desde = SelectField("desde", choices=getChoicesDesde(dbManager))
    # Campo Q_MONEDA_DESDE:
    Q_desde = FloatField("Q_desde")
    # Campo MONEDA_HASTA:
    hasta = SelectField("hasta",  choices=choices, validators=[DataRequired(message="Debe de informar la moneda que desea comprar"), Length(max=10)])
    # Campo Q_MONEDA_HASTA:
    Q_hasta = FloatField("Q_hasta")
    # Campo VALOR_PU:
    PU = FloatField("PU")


