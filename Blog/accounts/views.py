from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from accounts.models import Post,UserProfile
from accounts.forms import StatusUpdate,RegistrationForm
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    args = {'posts':posts}
    return render(request,'index.html',args)


def login_redirect(request):
    return redirect('login')

def update(request):
    if request.method == 'POST':
        form = StatusUpdate(request.POST)
        var1 = request.user
        var2 = UserProfile.objects.filter(user=var1)
        var3 = var2.values_list('profileimg').get()
        A = Post(username=request.user,Body= request.POST['Body'],profileimg=var3[0])
        A.save()
        return redirect('home')


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
        args={'form':form}
        return render(request, 'reg_form.html', args)
