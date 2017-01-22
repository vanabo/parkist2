from django import forms
from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker

from . models import Order, CallBack2

import datetime

class Order(ModelForm):
    class Meta:
        model = Order
        fields = ['current_point', 'current_date', 'current_time', 'phone4']
        widgets = {
            'current_time': DateTimePicker(options={"format": "HH:mm", "pickSeconds": False,
                                                    "pickDate": False},
                                           icon_attrs={'class': 'glyphicon glyphicon-time'},
                                           div_attrs={'class': 'input-group time'}),
            'current_date': DateTimePicker(options={"format": "DD-MM-YYYY", "pickTime": False}, icon_attrs = {'class': 'glyphicon glyphicon-date'},
                                           div_attrs = {'class': 'input-group date'}),
        }
    class Media:
        css = {
            'all': ('geoposition/css/geoposition.css',),
        }
        js = (
            'geoposition/js/geoposition.js',
        )


    def __init__(self, *args, **kwargs):
        kwargs.update(initial={
            'current_time': datetime.datetime.now()+datetime.timedelta(minutes=15),
            'current_date': datetime.date.today()
        })
        super(Order, self).__init__(*args, **kwargs)
        self.fields['phone4'].widget.attrs.update({
            'class': 'form-control',
            'id': 'phone',
        })

    def clean_current_time(self, *args, **kwargs):
        current_time = self.cleaned_data.get('current_time')
        if current_time < datetime.time(hour=8, minute=0, second=0, microsecond=0, tzinfo=None) or current_time > datetime.time(hour=20, minute=0, second=0, microsecond=0, tzinfo=None):
            raise forms.ValidationError('Введите, пожалуйста, требуемое время парковки в рабочие часы с 8:00 до 20:00')
        return current_time

class CallBack2(ModelForm):
    class Meta:
        model = CallBack2
        fields = ['name', 'phone']

    def __init__(self, *args, **kwargs):
        super(CallBack2, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'id': 'phone2',
        })
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
        })