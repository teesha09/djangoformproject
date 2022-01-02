from django.shortcuts import render
from django.http import HttpResponse
from .forms import q1

def index(request):
    var = "This is question 1, select your answer: "
    if request.method == "POST":
        form = q1(request.POST)
        if form.is_valid():
            field = form.cleaned_data['field']


    form = q1()
    return render (request, 'form.html', {'form': form})


ans = form.cleaned_data['field']
if ans == 'no':
    var = "This is question 2, if you answered no to question 1, select your answer: "
    return redirect (request, 'form.html', {'form': form})
else:
    var = "This is question 2, if you answered no to question 1, select your answer: "
    return redirect (request, 'form.html', {'form': form})


# def home_view(request):
#     context ={}
#     context['form']= InputForm()
#     return render(request, "home.html", context)
