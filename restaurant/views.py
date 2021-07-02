from django.shortcuts import redirect, render
from .models import food
from .forms import ReserveTableForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    foods = food.objects.all()
    return render(request,"index.html",{'foods' : foods})

def reserve(request):
    if request.method == 'POST':
        form = ReserveTableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully Reserved !')
            return redirect('/')
    else:
        form = ReserveTableForm()
        return render(request , 'reserve.html',{'form':form})

