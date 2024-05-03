from django.shortcuts import render
from .models import Category,Socccer
# Create your views here.

def get_info(request):
    categories = Category.objects.all()

    context = {'categories': categories,}
    return render(request, 'main.html', context=context)

def get_soccer(request, pk):
    soccers = Socccer.objects.filter(category=pk)
    context = {'soccers': soccers,} 
    return render(request,'soccer.html', context=context)
