from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import novostForm

# Create your views here.
data={
    'mass': ['Любимая музыка из игр','Мнение после прохождения Persona 5 Royal','Первый взгляд на геймплей Black Myth Wukong']
}
def index(request):
    return render(request,'main/Мой блог.html', data)
def about(request):
    return render(request, 'main/О себе.html')
def nier(request):
    return render(request, 'main/nier.html')
def persona(request):
    return render(request, 'main/persona.html')
def bmw(request):
    return render(request, 'main/bmw.html')
def create(request):
    error = None
    if request.method == 'POST':
        form = novostForm(request.POST, request.FILES)  # <-- добавлено request.FILES
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была заполнена неверно'
    else:
        form = novostForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', {'form': form, 'error': error})
