from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import JsonResponse


def welcome(request):
    return render(request, 'index1.html')

def json(request):
    comments = [
        {'first_name': 'Steve',
         'last_name': 'Jobs',
         'adress': '775 Westminster Avenue APT D5'},
        {'first_name': 'Bill',
         'last_name': 'Gates',
         'adress': ' 700 Carpenters Crossing APT D12'}
        ]

    return JsonResponse({'comments' : comments})


def resp(request):
    comments = [
        {'first_name': 'Steve',
         'last_name': 'Jobs',
         'adress': '775 Westminster Avenue APT D5'},
        {'first_name': 'Bill',
         'last_name': 'Gates',
         'adress': ' 700 Carpenters Crossing APT D12'}
        ]
    return HttpResponse(comments)

def html(request):
    comments = [
        {'first_name': 'Steve',
         'last_name': 'Jobs',
         'adress': '775 Westminster Avenue APT D5'},
        {'first_name': 'Bill',
         'last_name': 'Gates',
         'adress': ' 700 Carpenters Crossing APT D12'}
        ]

    context = {'comments' : comments}

    return render(request, 'index.html', context)