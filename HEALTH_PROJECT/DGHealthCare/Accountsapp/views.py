from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
def signupView(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            template = render_to_string('Accountsapp/email_template.html',{'name':request.POST.get('first_name')})  
            mail = request.POST.get('email')
            name = request.POST.get('first_name')
            email = EmailMessage('registration notification',template,settings.EMAIL_HOST_USER,[mail],)
            email.fall_silently = False
            email.send()
            return redirect('login')
    template_name = 'Accountsapp/signup.html'
    context={'form':form}
    return render(request,template_name,context)



def loginView(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pw')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            next = request.GET.get('next')
            if next is None:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('home')
            else:
                return redirect(next)
        else:
            messages.error(request,'invalid credentials please try again')
    template_name  = 'Accountsapp/login.html'
    context = {}
    return render(request,template_name,context)

def logoutView(request):
    request.session.clear()
    logout(request)
    return redirect('login')




