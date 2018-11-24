from django.shortcuts import render
from .forms import PayForm


def pay_products(request):
    if request.method == "POST":
        form = PayForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            data = form.cleaned_data
            
    
    return render(request,'products/generic.html')
