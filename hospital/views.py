from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

from profiles.models import Doctor, Nurse

def index(request):
    if not request.user.is_authenticated():
         return redirect('/login/?next=%s' % request.path)
    else:
        try:
            doctor = Doctor.objects.get(user=request.user)
            return redirect('doctor_profile')
        except ObjectDoesNotExist:
            try:
                nurse = Nurse.objects.get(user=request.user)
                return redirect('nurse_profile')
            except ObjectDoesNotExist:
                return redirect('/admin')
        # if doctor is not None:
        #     return redirect('doctor_profile')
        # elif Nurse.objects.get(user=request.user) is not None:
        #     return redirect('nurse_profile')
        # else:
        #     return redirect('admin') 
        # template = loader.get_template('profiles/doctor_main.html')
        # context = RequestContext(request) 
        # return HttpResponse(template.render(context))

def login_user(request):   
    state = ""   
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You are logged in"
                return redirect('index')
            else:
                state = "Your account has been disactivated"
        else:
            state = "Invalid login!"
    context = RequestContext(request)
    return render_to_response('registration/login.html',
                        {'state': state},
                        context_instance=context)

    # template = loader.get_template('registration/login.html')
    # context = RequestContext(request)
    # if request.POST:
    #     print "lslddsd"
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             redirect('/')
    #         else:
    #             redirect('/')
    #     else:
    #         redirect('/')
    # else:
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