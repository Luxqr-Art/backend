from django.shortcuts import render

def test_index(request):
    comments = [{
        'first_name' : 'Steve',
        'last_name' : 'Jobs',
        'adress' :'USA, City: New Castle State: DE (Delaware)',
    }]
    content_type = {'comments' : comments}
    return  render(request, 'test_index.html', content_type)
    # return JsonResponse({'comments':comments})