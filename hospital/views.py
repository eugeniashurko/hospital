from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login


def index(request):
    if not request.user.is_authenticated():
         return redirect('/login/?next=%s' % request.path)
    else:
        template = loader.get_template('profiles/doctor_main.html')
        context = RequestContext(request) 
        return HttpResponse(template.render(context))

# def login_view(request):      
#     template = loader.get_template('login.html')
#     context = RequestContext(request)
#     return HttpResponse(template.render(context))

def calendar(request):
    template = loader.get_template('calendar.html')
    context = RequestContext(request) 
    return HttpResponse(template.render(context)) 


def logout_view(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    else:
        logout(request)
        return redirect('/login')