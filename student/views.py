from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DetailView, DeleteView, FormView
from django.shortcuts import render, HttpResponse, redirect
from .models import Student
from student.forms import StudentForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'index.html')


def create(request):
    student_form = StudentForm()
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, 'Student has been created.')
            return redirect('view')
    context = {
        'student_form' : student_form
    }
    return render(request, 'create.html', context)

# Create with Class
class CreateStudent(CreateView):
    model = Student
    fields = ('name','surname','email','age')
    template_name = 'read.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('view')



def view(request):
    students = Student.objects.order_by('-name')
    context ={
        'students':students,
    }
    return render(request, 'view.html', context)


class ViewStudent(DetailView):
    model = Student
    fields = ('name','surname','email','age')
    template_name = 'single_student.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('view', kwargs={'pk',self.object.pk})

class ReadStudent(UpdateView):
    model = Student
    fields = ('name','surname','email','age')
    template_name = 'read.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('view')

class UpdateStudent(UpdateView):
    model = Student
    fields = ('name','surname','email','age')
    template_name = 'update.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('view')

def update_func(request,pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,  'update.html', context = {'form':form})


def delete_fnc(request,pk):
    try:
        delete_student = Student.objects.get(pk=pk)
        delete_student.delete()
        messages.success(request, '{} has been deleted.'.format(delete_student))
    except Student.DoesNotExist:
        return redirect('view')
    return redirect('view')

# if you use this function, it must be via POST, better use the function above
class DeleteStudent(DeleteView):
    model = Student
    fields = ('name','surname','email','age')
    template_name = 'delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('view')
