from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from django.template import loader

'''
def home(request):
    return HttpResponse("Hello, world. You're home.")
'''

def home(request):
    context = {
        
    }
    return render(request, 'app/main_page.html', context)
