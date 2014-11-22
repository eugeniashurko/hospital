from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login


def index(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    else:
        return HttpResponse("Hello, world. You're at the page index. %s" % request.user)

# def login_view(request):      
#     template = loader.get_template('login.html')
#     context = RequestContext(request)
#     return HttpResponse(template.render(context))


def logout_view(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    else:
        logout(request)
        return redirect('/login')