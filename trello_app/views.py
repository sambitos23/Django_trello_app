from django.shortcuts import render, redirect
from .models import TaskList, Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def index(request):
#     # this data is comming from database
#     lists = TaskList.objects.all()
#     tasks = Task.objects.all()
#     return render(request, 'trello_app/index.html', {'lists': lists, 'tasks': tasks})

# decorator: decorating your view with some additional logic, magically 
# if user is logged in then only show the add list page, otherwise redirect to login_url(redirection _url)
@login_required(login_url='login')
def create_list(request):
    if request.method == 'POST':
        # fetch the data and save it in he DB
        list_name = request.POST['list_name']
        # associat user
        list = TaskList(name = list_name, user=request.user)
        list.save()        
        # return render(request, 'trello_app/new_list.html')
        # return redirect('index')
        return redirect('home')
    else:    
        return render(request, 'trello_app/new_list.html')   

@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        #fetch the data and save it in the DB
        form = TaskForm(data=request.POST)
        # associat user
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            # return redirect('index')
            return redirect('home')
    else:
        form = TaskForm()   

    # same form object will get rendered in case of error
    return render(request, 'trello_app/new_task.html', {'form' : form})   
