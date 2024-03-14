from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Person

people = []

class Person:
    def _init_(self, username, password):
        self.username = username
        self.password = password

    def _str_(self):
        return self.username

def show_people(request):
    return render(request, 'index.html', {'people': people})

def add_person(request):
    if request.method == 'POST':
        form = Person(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person(username=username, password=password)
            people.append(person)
            return HttpResponseRedirect('/')
    else:
        form = Person()
        return render(request, 'add.html', {'form': form, 'people': people})
