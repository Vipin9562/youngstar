from django.http import HttpResponse
from django.shortcuts import render
from .models import movie


# Create your views here.
def index(request):
    person = movie.objects.all()
    context = {'person': person}
    return render(request, 'index.html', context)


def detail(request, person_id):
    person = movie.objects.get(id=person_id)
    return render(request, 'detail.html', {'person': person})


def add_person(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        house_name = request.POST.get('house_name', )
        phone_number = request.POST.get('phone_number', )
        img = request.FILES['img']
        person = movie(name=name, house_name=house_name, phone_number=phone_number, img=img)
        person.save()
    return render(request, 'add.html')


def regi(request, person_id):
    person = movie.objects.get(id=person_id)
    return render(request, 'register.html', {'person': person})




