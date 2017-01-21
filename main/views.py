from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from smsaero import SmsAero

from .forms import Order
from .forms import CallBack2

api = SmsAero(u'nadezhda.valyaeva@gmail.com', u'uto9inuto9in')

def index(request):
    form = Order(request.POST or None)
    success = ''
    if form.is_valid():
        form_current_point = form.cleaned_data.get('current_point')
        form_current_date = form.cleaned_data.get('current_date')
        form_current_time = form.cleaned_data.get('current_time')
        form_phone3 = form.cleaned_data.get('phone3')
        subject = 'Parkist Заказ'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'igamer@mail.ru', '5067618@mail.ru']

        form_phone32 = '7' + form_phone3.replace("-", "")
        to_phone = '{0}'.format(form_phone32)
        contact_message = '{0} {1} {2} {3}'.format(form_current_point, form_current_date, form_current_time, to_phone)
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=True,
        )

        api.send(
            to_phone,
            'Спасибо за Ваш Заказ. Ожидайте звонка в течение 1 минуты. Call-центр: 8-495-506-76-18'
        )

        api.sendtogroup(
            'main_group',
            contact_message
        )

        success = 'Мы получили Вашу заявку. Ожидайте звонка!'


    form2 = CallBack2(request.POST or None)
    success2 = ''
    if form2.is_valid():
        form2_name = form2.cleaned_data.get('name')
        form2_phone = form2.cleaned_data.get('phone')
        form22_phone = form2_phone.replace("-", "")
        to_phone2 = '{0}'.format(form22_phone)
        subject3 = 'Parkist Обратный звонок'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'igamer@mail.ru', '5067618@mail.ru']
        contact_message3 = '{0} {1}'.format(form2_name, to_phone2)
        send_mail(
            subject3,
            contact_message3,
            from_email,
            to_email,
            fail_silently=True,
        )

        api.sendtogroup(
            'main_group',
            contact_message3
        )

        success2 = 'Спасибо за заявку! Ждите звонка!'


    context = {
        'form': form,
        'form2': form2,
        'success': success,
        'success2': success2
    }

    return render(request, 'main/index.html', context)
