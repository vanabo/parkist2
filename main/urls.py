from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^become-parkist$', views.become_parkist, name='become_parkist'),
    url(r'^legal/termsofuse$', views.termsofuse, name='termsofuse')
]