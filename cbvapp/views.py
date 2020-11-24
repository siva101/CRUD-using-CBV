from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Student
from django.urls import reverse_lazy


'''
class Cbv(View):
    def get(self,request):
        return HttpResponse('<h1> Class Based View</h1>')
'''


class StudentListView(ListView):
        model=Student

class StudentDetailView(DetailView):
        model=Student

class StudentCreateView(CreateView):
        model=Student
        fields='__all__'

class StudentUpdateView(UpdateView):
        model=Student
        fields='__all__'


class StudentDeleteView(DeleteView):
        model = Student
        success_url=reverse_lazy('home')
