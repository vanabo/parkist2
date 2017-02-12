from django import forms
from django.forms import ModelForm

from . models import Order, CallBack2

import datetime

date = datetime.date.today()
time = datetime.datetime.now()

if date.isoweekday() == 6 or date.isoweekday() == 7:
    ttime = datetime.time(hour=12, minute=0, second=0, microsecond=0, tzinfo=None)
    tdate = datetime.date.today()
elif (date.isoweekday() == 1 or date.isoweekday() == 2 or date.isoweekday() == 3 or date.isoweekday() == 4 or date.isoweekday() == 5) \
        and (time.hour == 0 or time.hour == 1 or time.hour == 2 or time.hour == 3 or time.hour == 4 or time.hour == 5 or time.hour == 6
        or time.hour == 7 or time.hour == 8 or time.hour == 9 or time.hour == 10 or time.hour == 11 or time.hour == 22 or time.hour == 23):
    ttime = datetime.time(hour=12, minute=0, second=0, microsecond=0, tzinfo=None)
    tdate = datetime.date.today()
elif (date.isoweekday() == 1 or date.isoweekday() == 2 or date.isoweekday() == 3 or date.isoweekday() == 4 or date.isoweekday() == 5) \
        and (time.hour == 22 or time.hour == 23 or time.hour == 20 or time.hour == 21):
    ttime = datetime.time(hour=12, minute=0, second=0, microsecond=0, tzinfo=None)
    tdate = datetime.date.today()
else:
    ttime = datetime.datetime.now()+datetime.timedelta(minutes=30)
    tdate = datetime.date.today()

class Order(ModelForm):
    class Meta:
        model = Order
        fields = ['current_point', 'current_date', 'current_time', 'phone4', 'promo']
        #widgets = {
            #'current_time': DateTimePicker(options={"format": "HH:mm", "pickSeconds": False,
                                                    #"pickDate": False},
                                           #icon_attrs={'class': 'glyphicon glyphicon-time'},
                                           #div_attrs={'class': 'input-group time'}),
            #'current_date': DateTimePicker(options={"format": "DD.MM.YYYY", "pickTime": False}, icon_attrs = {'class': 'glyphicon glyphicon-date'},
                                          # div_attrs = {'class': 'input-group date'}),
        #}
    class Media:
        css = {
            'all': ('geoposition/css/geoposition.css',),
        }
        js = (
            'geoposition/js/geoposition.js',
        )


    def __init__(self, *args, **kwargs):
        kwargs.update(initial={
            'current_time': ttime,
            'current_date': tdate,
        })
        super(Order, self).__init__(*args, **kwargs)
        self.fields['phone4'].widget.attrs.update({
            'class': 'form-control',
            'id': 'phone',
        })
        self.fields['current_date'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['current_time'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['promo'].widget.attrs.update({
            'class': 'form-control',
        })

    #def clean_current_time(self, *args, **kwargs):
        #current_time = self.cleaned_data.get('current_time')
        #if current_time < datetime.time(hour=8, minute=0, second=0, microsecond=0, tzinfo=None) or current_time > datetime.time(hour=20, minute=0, second=0, microsecond=0, tzinfo=None):
            #raise forms.ValidationError('Введите, пожалуйста, требуемое время парковки в рабочие часы с 8:00 до 20:00')
        #return current_time

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