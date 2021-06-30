from django.shortcuts import redirect, render
from .models import food
from .forms import ReserveTableForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    
    foods = food.objects.all()

    return render(request,"index.html",{'foods' : foods})

def reserve(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            print("user created")
    
            return redirect('/')
    
        else :
            return render(request , 'reserve.html')

