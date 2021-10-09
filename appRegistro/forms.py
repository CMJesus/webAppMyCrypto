from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, FloatField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

import datetime

def validar_fecha(formulario, campo):
    hoy = datetime.datime.today()
    if campo.data > hoy:
        raise ValidationError("La fecha no puede ser posterior a hoy")

#Herencia desde librería, mucha funcionalidad
class MovimientoFormulario(FlaskForm):

    id = HiddenField()
    
    date = DateField("date", validators=[DataRequired(message="Debe de informar la fecha"), validar_fecha])
    time = StringField("time", validators=[DataRequired(message="Debe de informar sobre la hora")])
    desde = SelectField("desde", choices=[('EUR', 'Euro'), ('BTC', 'Bitcoin')], validators=[DataRequired(message="Debe de informar la moneda en que desea adquirir"), Length(max=10)])
    Q_desde = FloatField("Q_desde", validators=[DataRequired(message="Debe de informar una cantidad")])
    hasta = StringField("hasta", validators=[DataRequired(message="Debe de informar la moneda que desea comprar"), Length(max=10)])
    Q_hasta = FloatField("Q_hasta", validators=[DataRequired(message="Debe de informar una cantidad")])
    PU = FloatField("PU", validators=[DataRequired(message="Debe de informar una cantidad")])

    
    
    
    #                                                 NumberRange(message="Debe de informar un importe positivo", min=0.01)])
    # ingreso_gasto = RadioField(validators=[DataRequired(message="Debe de informar tipo de movimiento")], 
    #                                         choices=[('G', 'Gasto'), ('I', 'Ingreso')])
    submit = SubmitField('Aceptar')

    def validate_fecha(self, campo):
        hoy = datetime.datime.today()
        if campo.data > hoy:
            raise ValidationError("La fecha no puede ser posterior a hoy")
