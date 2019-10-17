from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to blog app</h1><a href='/app1/'>APP1</a></h1>")

def about(request,user):
    return HttpResponse("<h1 style='color:red;font-size:3-px'>Welcome user {}</h1>".format(user))