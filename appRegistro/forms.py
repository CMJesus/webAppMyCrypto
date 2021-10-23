from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, RadioField, SubmitField, SelectField, FloatField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from appRegistro.models import DBManager
import datetime
from appRegistro import app
from appRegistro.queriesDB import getSaldo


choices=[('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), 
        ('TRX', 'Tron'), ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), ('BCHSV', 'BitcoinSV'), ('USDT', 'StDolar'), ('BSV', 'Bsv'), ('ADA', 'Cardano')]


def getChoicesDesde(dbManager):
    stockChoices=[('EUR', 'Euro')]

    for choice in choices:
        if choice[0] != "EUR":

            saldoCrypto = getSaldo(dbManager, choice[0])
            if saldoCrypto > 0:
                stockChoices.append(choice)        
    return stockChoices


def date_validate(formulario, campo):
    hoy = datetime.date.today()
    if campo.data > hoy:
        raise ValidationError("La fecha no puede ser posterior a hoy")


#Herencia desde librería, mucha funcionalidad
class MovimientoFormulario(FlaskForm):
    ruta_basedatos = app.config.get("RUTA_BASE_DATOS")
    dbManager = DBManager(ruta_basedatos)
    id = HiddenField()
    
    date = DateField("date", validators=[DataRequired(message="Debe de introducir una fecha"), date_validate])
    
    time = StringField("time", validators=[DataRequired(message="Debe de informar sobre la hora")])
    
    desde = SelectField("desde", choices=getChoicesDesde(dbManager))
    
    Q_desde = FloatField("Q_desde", validators=[DataRequired(message="Debe de informar una cantidad")])
    
    hasta = SelectField("hasta",  choices=choices, validators=[DataRequired(message="Debe de informar la moneda que desea comprar"), Length(max=10)])
    
    Q_hasta = FloatField("Q_hasta")
    
    PU = FloatField("PU")



# Gestión de errores con el cálculo, para la consulta, y del envío, para que haga 
# el reenvío en condiciones

