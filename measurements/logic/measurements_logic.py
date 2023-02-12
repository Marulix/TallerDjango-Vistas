from ..models import Variable
from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(meas_pk):
    measurement = Measurement.objects.get(pk=meas_pk)
    return measurement

def update_measurement(meas_pk, new_var):
    measurement = get_measurement(meas_pk)
    variable_pk = Variable.objects.get(pk=new_var["variable"])
    measurement.variable = variable_pk
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.save()
    return measurement

def create_measurement(measurement):
    variable_pk = Variable.objects.get(pk=measurement["variable"])
    measurement = Measurement(variable=variable_pk, 
                              value=measurement["value"], 
                              unit=measurement["unit"], 
                              place=measurement["place"])
    measurement.save()
    return measurement

def delete_measurement(meas_pk):
    measurement = get_measurement(meas_pk)
    measurement.delete()
    return measurement

