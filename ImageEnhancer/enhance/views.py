from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.
def enhance_home(request):

    return render(request, 'enhance/Web_Site/ImageEnhancer.html')