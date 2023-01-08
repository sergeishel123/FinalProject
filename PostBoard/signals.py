from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib.auth import login

"""
@receiver(user_signed_up,dispatch_uid = 'some.unique.string.id.for.allauth.user_signed_up')
def user_signed_up(request,user,**kwargs):
    send_mail(
        subject = 'Тестовое письмо',
        message = 'Потвердите регистрацию',
        from_email = 'sergeiazharkov@yandex.ru',
        recipient_list = ['agaverdyevsergej@gmail.com','agaverdyevaira@gmail.com']
    )
    redirect(to = 'categories/')
"""
