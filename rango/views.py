from django.shortcuts import render


def index(request):
    '''Index view.'''
    context_dict = {'boldmessage': 'I am bold font from the context'}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    '''About view.'''
    context_dict = {'boldmessage': 'I am bold font from the context'}
    return render(request, 'rango/about.html', context_dict)
