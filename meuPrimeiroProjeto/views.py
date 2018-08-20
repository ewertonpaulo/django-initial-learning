from django.http import HttpResponse

def hello(request):
    return HttpResponse("helloWorld")

def articles(request, year):
    return HttpResponse('O ano enviado foi '+str(year))