from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def envia_email(request):
    send_mail('Assunto', 'Esse é o email que estou te enviando', 'matheus.granda@gmail.com', ['lo_granda@hotmail.com', 'matheus.granda@gmail.com'])
    return HttpResponse('Olá!')