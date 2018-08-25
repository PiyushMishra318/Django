from django.shortcuts import render,redirect,HttpResponse
from myapp.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from myapp.models import UserProfile
# Create your views here.
def home(request):
    return render(request,'index.html')


def login_redirect(request):
    return redirect('/login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

        args={'form':form}
        return render(request, 'reg_form.html', args)

def searchprofile(request):
    if (request.method == 'POST'):
        try:
            search1 = request.POST.get('profilename')
            search2 = UserProfile.objects.filter(username=search1)
            search3 = search2.values_list('username','profileimg').get()
            return render(request, 'index.html',{'search3':search3})
        except UserProfile.DoesNotExist:
            return render(request,'error.html')
