from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi '+str(year))

def ler_do_banco(nome):
    lista_nomes = [
        {'nome': 'ana', 'idade':21},
        {'nome': 'joao', 'idade': 22},
        {'nome': 'ana3', 'idade': 23}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome': 'não encontrado', 'idade':0}

def fname(request, nome):
    result = ler_do_banco(nome)
    print(result)
    if result['idade']>0:
        return HttpResponse(str(result['idade']))
    else:
        return HttpResponse('pessoa não encontrada')

def fname2(request, nome):
    idade = ler_do_banco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade':idade})