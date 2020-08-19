from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import JsonResponse

comments = [
        {'first_name': 'Steve',
         'last_name': 'Jobs',
         'adress': '775 Westminster Avenue APT D5'},
        {'first_name': 'Bill',
         'last_name': 'Gates',
         'adress': ' 700 Carpenters Crossing APT D12'}
        ]
def welcome(request):
    return render(request, 'index1.html')

def json(request):
    return JsonResponse(comments, safe=False)

def resp(request):
   return HttpResponse(comments, content_type='application/json')

def html(request):
    context = {'comments' : comments}

    return render(request, 'index.html', context)