from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
from .models import AddUser
# Create your views here.
def index(request):
    return render(request,"app1/header.html")
    #return HttpResponse("<h1 style='color:red'>Welcome to app1</h1>")
def login(request):
    if request.session.get('email'):
        error = "Already logged in"
        return render(request,"app1/data.html",{'error':error})
    else:
        form = Login()
        return render(request,"app1/login.html",{'form':form})

def login1(request):
    form1 = Login(request.POST)
    if form1.is_valid():
        if request.method == "POST":
            email = form1.cleaned_data['email']
            try:
                user = AddUser.objects.get(email=email)
            except AddUser.DoesNotExist as e:
                error = "User does not exist...Try again.."
                form = Login()
                return render(request,"app1/login.html",{'error':error,'form':form})
            else:
    
                password = form1.cleaned_data['password']
                password1 = user.password
                if password == password1:
                    request.session['email'] = email
                    request.session['islogin'] = "True"
                    return render(request,"app1/data.html")
                    #return HttpResponse("<h1>Welcome user with email {}".format(email))
                else:
                    error = "Password does not match...Try again"
                    form = Login()
                    return render(request,"app1/login.html",{'error':error,'form':form})
    
        else:
            error = "Method incorrect"
            form = Login()
            return render(request,"app1/login.html",{'error':error,'form':form})
    else:
        error = "Form invalid"
        form = Login()
        return render(request,"app1/login.html",{'error':error,'form':form})

def signup(request):
    form = Signup()
    return render(request,'app1/signup.html',{'form':form})


class Signedup(View):
    def get(self,request):
        error = "Invalid method"
        form = Signup()
        return render(request,"app1/signup.html",{'error':error,'form':form})
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            pass1 = form.cleaned_data['password']
            pass2 = form.cleaned_data['confirm_password']
            if pass1 == pass2:
                dict = {
                    'firstname' : form.cleaned_data['firstname'],
                    'lastname' : form.cleaned_data['lastname'],
                    'username' : form.cleaned_data['username'],
                    'email' : form.cleaned_data['email'],
                    'password' : form.cleaned_data['password'],
                    'pic' : form.cleaned_data['pic'],
                }
                new_user = AddUser.objects.create(**dict)
                new_user.save()
                return render(request,"app1/data.html",{'data':dict})
            else:
                error = "Password does not match..Try again.."
                form = Signup()
                return render(request,"app1/signup.html",{'form':form,'error':error})
        else:
            error = "Invalid form..."
            form = Signup()
            return render(request,"app1/signup.html",{'form':form,'error':error})


def logout(request):
    del request.session['email']
    del request.session['islogin']
    form = Login()
    return render(request,"app1/login.html",{'form':form})