from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, FloatField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

import datetime

def validar_fecha(formulario, campo):
    ahora = datetime.date.today()
    if campo.data > ahora:
        raise ValidationError("La fecha no puede ser posterior a hoy")

#Herencia desde librería, mucha funcionalidad
class MovimientoFormulario(FlaskForm):

    id = HiddenField()
    
    date = DateField("date", validators=[DataRequired(message="Debe de introducir una fecha"), validar_fecha])
    time = StringField("time", validators=[DataRequired(message="Debe de informar sobre la hora")])
    desde = SelectField("desde", choices=[('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), ('TRX', 'Tron'), 
    ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), ('BCH', 'Bch'), ('USDT', 'StDolar'), ('BSV', 'Bsv'), ('ADA', 'Cardano')], validators=[DataRequired(message="Debe de informar la moneda en que desea adquirir"), Length(max=10)])
    Q_desde = FloatField("Q_desde", validators=[DataRequired(message="Debe de informar una cantidad")])
    hasta = SelectField("hasta",  choices=[('EUR', 'Euro'), ('ETH', 'Ethereum'), ('LTC', 'Litecoin'), ('BNB', 'Binance'), ('EOS', 'EOS'), ('XLM', 'Stellar'), ('TRX', 'Tron'), 
    ('BTC', 'Bitcoin'), ('XRP', 'Ripple'), ('BCH', 'Bch'), ('USDT', 'StDolar'), ('BSV', 'Bsv'), ('ADA', 'Cardano')], validators=[DataRequired(message="Debe de informar la moneda que desea comprar"), Length(max=10)])
    Q_hasta = FloatField("Q_hasta", validators=[DataRequired(message="Debe de informar una cantidad")])
    
    #Este debe de dar un resultado informativo, no para insertar
    PU = FloatField("PU", validators=[DataRequired(message="Debe de informar una cantidad")])

    # Ver si es un submit o no
    # submit = SubmitField('Calcular')    
    submit = SubmitField('Enviar')


