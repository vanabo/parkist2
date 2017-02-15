from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from smsaero import SmsAero
import requests
import random

from .forms import Order
from .forms import CallBack2
from .forms import Promo

def index(request):
    form = Order(request.POST or None)
    success = ''
    if form.is_valid():
        form_current_point = form.cleaned_data.get('current_point')
        form_current_date = form.cleaned_data.get('current_date')
        form_current_time = form.cleaned_data.get('current_time')
        form_phone4 = form.cleaned_data.get('phone4')
        form_promo = form.cleaned_data.get('promo')
        subject = 'Parkist Заказ'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'igamer@mail.ru', '5067618@mail.ru', 'rlionia@gmail.com', 'ilyagamer@icloud.com']
        form_phone42 = form_phone4.replace("-", "").replace(" ", "").replace("+", "").replace("(", "").replace(")", "")
        to_phone = '{0}'.format(form_phone42)
        lat = '{0}'.format(form_current_point[0])
        lon = '{0}'.format(form_current_point[1])
        coord = {'lat':  lat, 'lon': lon}
        map = 'https://www.maps.yandex.ru/?pt={lon},{lat}&zoom=13&l=map'.format(**coord)
        geo = 'geo:{lat},{lon}?z=17'.format(**coord)
        contact_message = '{0} {1} {2} {3} {4} {5}'.format(form_current_point, form_current_date, form_current_time, to_phone, map, form_promo)
        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=True,
        )

        payload2 = {'user': 'nadezhda.valyaeva@gmail.com', 'password': '1522ynMqc2QlyVXSclSLWqYaMwMy', 'from': 'NEWS',
                    'to': to_phone, 'text': 'Мы получили Вашу заявку. С Вами свяжется Паркист в течение 2 минут. Call-центр: 8(495)506-76-18'}
        r2 = requests.get("https://gate.smsaero.ru/send/", params=payload2)

        payload3 = {'user': 'nadezhda.valyaeva@gmail.com', 'password': '1522ynMqc2QlyVXSclSLWqYaMwMy', 'from': 'NEWS',
                    'group': 'main_group', 'text': contact_message}
        r3 = requests.get("https://gate.smsaero.ru/sendtogroup/", params=payload3)

        success = 'Мы получили Вашу заявку. Ожидайте звонка!'


    form2 = CallBack2(request.POST or None)
    success2 = ''
    if form2.is_valid():
        form2_name = form2.cleaned_data.get('name')
        form2_phone = form2.cleaned_data.get('phone')
        form22_phone = form2_phone.replace("-", "").replace(" ", "").replace("+", "").replace("(", "").replace(")", "")
        to_phone2 = '{0}'.format(form22_phone)
        subject3 = 'Parkist Обратный звонок'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'igamer@mail.ru', '5067618@mail.ru', 'rlionia@gmail.com', 'ilyagamer@icloud.com']
        contact_message3 = '{0} {1}'.format(form2_name, to_phone2)
        send_mail(
            subject3,
            contact_message3,
            from_email,
            to_email,
            fail_silently=True,
        )

        payload1 = {'user': 'nadezhda.valyaeva@gmail.com', 'password': '1522ynMqc2QlyVXSclSLWqYaMwMy', 'from': 'NEWS',
                   'group': 'main_group', 'text': contact_message3}
        r1 = requests.get("https://gate.smsaero.ru/sendtogroup/", params=payload1)

        success2 = 'Спасибо за заявку! Ждите звонка!'

    form3 = Promo(request.POST or None)
    success3 = ''
    if form3.is_valid():
        form3_email = form3.cleaned_data.get('email')
        form3_phone2 = form3.cleaned_data.get('phone2')
        form32_phone2 = form3_phone2.replace("-", "").replace(" ", "").replace("+", "").replace("(", "").replace(")", "")
        to_email2 = ['{0}'.format(form3_email)]
        to_phone3 = '{0}'.format(form32_phone2)
        subject4 = 'Parkist Промокод'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['nv@alltargets.ru', 'igamer@mail.ru', '5067618@mail.ru', 'rlionia@gmail.com',
                    'ilyagamer@icloud.com']
        code = random.randint(0, 10000)
        promo = 'CAR' + str(code)
        message = '{0} {1}'.format('Промокод на бесплатную парковку', promo)
        contact_message3 = '{0} {1} {2}'.format(form3_email, to_phone3, message)


        send_mail(
            subject4,
            contact_message3,
            from_email,
            to_email,
            fail_silently=True,
        )
        if to_email2:
            send_mail(
                subject4,
                message,
                from_email,
                to_email2,
                fail_silently=True,
            )

        payload = {'user': 'nadezhda.valyaeva@gmail.com', 'password': '1522ynMqc2QlyVXSclSLWqYaMwMy', 'from': 'NEWS', 'to': to_phone3, 'text': message}
        r = requests.get("https://gate.smsaero.ru/send/", params=payload)

        success3 = 'Промокод отправлен. Спасибо за Вашу заявку!'


    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'success': success,
        'success2': success2,
        'success3': success3,
    }

    return render(request, 'main/index.html', context)

def faq(request):
    context = {}
    return render(request, 'main/faq.html', context)

def for_business(request):
    context = {}
    return render(request, 'main/for-business.html', context)

def become_parkist(request):
    context = {}
    return render(request, 'main/become-parkist.html', context)

def termsofuse(request):
    context = {}
    return render(request, 'main/termsofuse.html', context)