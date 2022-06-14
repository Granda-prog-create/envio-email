Projeto de envio de emails utilizando Django
Para iniciar o projeto, digite django-admin startproject (nome do projeto) .
O "." é para não haver redundâncias nos arquivos. 
A seguir, use: python manage.py  startapp envia_email.  
pip install python-decouple
Em settings.py, fiz as seguintes alterações:

Linha 125  
#Email 
DEFAULT_FROM_EMAIL = "matheus.granda@gmail.com"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')



