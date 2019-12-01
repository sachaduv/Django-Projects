from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm,TodoModelForm
from django.views.decorators.http import require_POST  

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    form = TodoModelForm()
    context={'todos':todos,'form':form}
    return render(request,'todo/index.html',context)

@require_POST
def addTask(request):
    #form = TodoForm(request.POST)
    #update_form = Todo.objects.get(pk=17)
    #model_form = TodoModelForm(request.POST,instance=update_form)
    model_form = TodoModelForm(request.POST)
    if model_form.is_valid():
        # todo_task=Todo(task=form.cleaned_data['task'])
        # todo_task.save()
        model_form.save()
    return redirect('index')

def complete(request,todo_id):
    complete_flag = Todo.objects.get(pk=todo_id)
    complete_flag.complete=True
    complete_flag.save()
    return redirect('index')

def delete_complete(request):
    delete_flag=Todo.objects.filter(complete__exact=True)
    delete_flag.delete()
    return redirect('index')

def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')