from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def htmx_content(request):
    response =  render(request, 'partials/user-table.html')
    response['HX-Trigger'] = 'custom-event'
    return response
