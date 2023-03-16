from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

# class List View

class TaskListview(ListView):
    model = Task      # model name
    template_name = 'index.html'
    context_object_name = 'task'

# class Detailed View

class TaskDetailsview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'i'

# class update View

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('Todo_App:cbvdetails', kwargs={'pk': self.object.id})

# class Delete View

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('Todo_App:cbvhome')


#Function View

def index(request):
    taskd = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        taskr = Task(name=name, priority=priority, date=date)
        taskr.save()
    return render(request, 'index.html', {'task': taskd})
def delete(request,ID):
    task = Task.objects.get(id=ID)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')
def update(request,ID):
    task = Task.objects.get(id=ID)
    f = TodoForms(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'task': task, 'f': f})
