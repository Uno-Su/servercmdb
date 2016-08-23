from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return HttpResponse("Hello Index!")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

@csrf_exempt
def Login(request):
    error = ""
    if request.method == 'GET':
        return render_to_response('login.html',locals())
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        if username and password:
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render_to_response("index.html")
                else:
                    error = "User is not active"
            else:
                error = "user is not existed"
        else:
            error = "user or password error "
    return render_to_response('login.html', {'error': error})
