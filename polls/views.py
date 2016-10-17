from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from polls.models import User
from polls.api import salt_crypt

# Create your views here.


def Login(request):
    error = ""
    users = User.objects.all()
    if request.method == 'GET':

        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = User.objects.get(username=username)
                if user.username == username and user.password == salt_crypt(password, "mysalt"):

                    request.session['login'] = True
                    response = render(request, 'index.html', {'users': users})
                    response.set_cookie('status', 'login')
                    return response
                else:
                    error = "user or password error "
            except User.DoesNotExist:
                error = "user is not existed"
    return render(request, 'login.html', {'error': error})


@login_required(login_url='/login/')
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


def Logout(request):
    # logout(request)
    request.session.flush()
    return redirect(reverse("login"))


def signup(request):
    error = ""
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email', '')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        print(username)
        print(email)
        print(password)
        print(repassword)
        if password != repassword:
            error = "两次输入的密码不同"
        else:
            db_user = User.objects.filter(username=username)
            print(db_user)
            if User.objects.filter(username=username):
                error = "用户名%s已存在" % username
            else:
                add_user = User(username=username, email=email, password=salt_crypt(password, "mysalt"))
                add_user.save()
                return redirect(reverse('index'))
    return render(request, 'signup.html', {'error': error})



