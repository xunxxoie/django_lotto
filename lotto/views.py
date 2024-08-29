from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):
    
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})

def post(request):
    
    if request.method == "POST":
        form = PostForm(request.POST) # request.POST -> POST 쿼리의 name:value
        
        if form.is_valid(): #request value is compatible with db form?
            lotto = form.save(commit=False) # middle save but not in db(value = db cols)
            lotto.generate()
            
            return redirect('index')
        
        
    form = PostForm()
    return render(request, "lotto/form.html", {'form' : form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request,"lotto/detail.html", {'lotto':lotto})
    

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, World</h1>")