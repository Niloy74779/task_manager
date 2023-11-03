from django.shortcuts import render
from .models import AddTask
from .forms import AddTaskForm
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect



# Create your views here.

def search_blog(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        venues = AddTask.objects.filter(title__icontains=searched)
        return render(request, 'search.html', {'searched':searched, 'venues':venues})
    else:
        return render(request, 'search.html', {})


class Taskview(ListView):
    model = AddTask
    template_name = 'task.html'
    ordering = ['-updated_at']
    
    def get_queryset(self):
        return AddTask.objects.filter(is_complete=False)
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = AddTask.objects.all()
        context = super(Taskview, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu 
        return context
    

class AddTaskView(CreateView):
    model = AddTask
    form_class = AddTaskForm
    template_name = 'add_task.html'
    
class UpdateTaskview(UpdateView):
    model = AddTask
    fields = ['title', 'description']
    template_name = 'add_task.html'
    def get_success_url(self):
        return reverse_lazy('task') 
    
class DeleteTaskview(DeleteView):
    model = AddTask
    template_name = 'task.html'
    def get_success_url(self):
        return reverse_lazy('task') 
    
class CompletedTasksView(ListView):
    model = AddTask
    template_name = 'complete_task.html'

    def get_queryset(self):
        return AddTask.objects.filter(is_complete=True)

class CompleteTask(View):
    def get(self, request, id):
        task = AddTask.objects.get(pk=id)
        task.is_complete = True
        task.save()
        return redirect("completed")
    
class InCompleteTask(View):
    def get(self, request, id):
        task = AddTask.objects.get(pk=id)
        task.is_complete = False
        task.save()
        return redirect("task")
    
    
