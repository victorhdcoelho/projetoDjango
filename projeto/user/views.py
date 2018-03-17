from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def list_users(request):
    user = User.objects.all()
    data = {}
    data['object_list'] = user
    return render(request,'user.html',data)

def create_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request,'users-form-new.html',{'form': form})

def update_user(request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance= user)
    if form.is_valid():
        form.save()
        return redirect('list_users')
    return render(request,'users-form.html',{'form': form})

def delete_user(request, pk):
    users = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        user.delete()
        return redirect('list_users')
    return render(request,'users-form.html', {'object':user})

# Create your views here.
