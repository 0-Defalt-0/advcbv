from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from basic_app.models import School, Student
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['injectme'] = "Rushi is the best teacher"
		return context


class SchoolListView(ListView):
	model = School
	#returns school_list
	context_object_name = 'schools'

class SchoolDetailView(DetailView):
	model = School
	context_object_name = 'school_details'
	template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
	fields = ('name','principal','location')
	model = School

class SchoolUpdateView(UpdateView):
	fields = ('name', 'principal')
	model  = School

class SchoolDeleteView(DeleteView):
	model = School
	success_url = reverse_lazy("basic_app:list")
	context_object_name = 'school'
