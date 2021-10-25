from flask import flash
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, SubmitField, SelectField, FloatField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from appRegistro.models import DBManager
import datetime
from appRegistro import app
from appRegistro.queriesDB import getSaldo

# VARIABLE GLOBAL: "choices".
choices=[
    ('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), 
    ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), ('TRX', 'Tron'), 
    ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), ('BCH', 'Bitcoin Cash'), ('USDT', 
    'StDolar'), ('BCHSV', 'Bitcoin SV'), ('ADA', 'Cardano')
        ]

# CLASE MOVIMIENTO_FORMULARIO: 
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
    
    # FUNCIÓN GET_CHOICES_DESDE.
    # Proceso: selecciona las monedas que disponen de crédito:
    @classmethod
    def getChoicesDesde(cls):
        # Euro constante.
        stockChoices=[('EUR', 'Euro')]
        # Este bucle iterará en la lista de tuplas "choices".
        for choice in choices:
            if choice[0] != "EUR":
                # Llamamos a la función getSaldo:
                saldoCrypto = getSaldo(cls.dbManager, choice[0])
                if saldoCrypto > 0:
                    stockChoices.append(choice)
        #print(stockChoices)        
        return stockChoices

# ************************************************************
# ----------------------Formulario----------------------------
# ************************************************************
    # Campo FECHA:
    date = DateField("Fecha:", validators=[DataRequired(message="Debe de introducir una fecha"), date_validate])
    # Campo TIEMPO:
    time = StringField("Hora:", validators=[DataRequired(message="Debe de informar sobre la hora")])
    # Campo MONEDA_DESDE: no me acepta float.
    desde = SelectField("Moneda desde la que desea hacer su inversión:", choices=choices)
    # Campo Q_MONEDA_DESDE:
    Q_desde = FloatField("Importe a invertir:")
    # Campo MONEDA_HASTA:
    hasta = SelectField("Moneda que desea adquirir:", choices=choices, validators=[DataRequired(message="Debe de informar la moneda que desea comprar"), Length(max=10)])
    # Campo Q_MONEDA_HASTA:
    Q_hasta = FloatField("Cantidad de unidades adquiridas:")
    # Campo VALOR_PU:
    PU = FloatField("Precio Unitario por moneda invertida (rate):")


