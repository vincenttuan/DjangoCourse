import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello Django !")


def hello_name(request, name):
    age = 0
    try:
        age = request.GET['age'] # ?age=300
        age = int(age)
    except:
        pass
    return HttpResponse("Hello %s %d !" % (name, age))


def hello_op(request, op, x, y):
    if op == 'add':
        return HttpResponse("%d %s %d = %d" % (x, op, y, (x + y)))
    elif op == 'sub':
        return HttpResponse("%d %s %d = %d" % (x, op, y, (x - y)))
    elif op == 'mul':
        return HttpResponse("%d %s %d = %d" % (x, op, y, (x * y)))
    elif op == 'div':
        return HttpResponse("%d %s %d = %.1f" % (x, op, y, (x / y)))


def page_user(request, name):
    dict = {'name':name, 'age':30}
    return render(request, 'page_user.html', dict)


def page_bmi(request, name):
    h = request.GET['h']
    w = request.GET['w']
    bmi = float(w)/(float(h)/100)**2
    bmi_str = '%.2f' % bmi
    now = datetime.datetime.now()
    dict = {'name':name, 'h':h, 'w':w, 'bmi':bmi, 'now':now, 'bmi_str':bmi_str}
    return render(request, 'page_bmi.html', dict)


def page_users(request):
    users = [
        {'name': 'vincent', 'age': 30},
        {'name': 'anita', 'age': 28},
        {'name': 'howard', 'age': 15},
        {'name': 'joanna', 'age': 10}
    ]
    dict = {}
    dict['users'] = users
    return render(request, 'page_users.html', dict)


def page_polls(request):
    poll_name = '水果大調查'
    polls = [
        {'name': '蓮霧', 'poll': random.randint(0, 100)},
        {'name': '西瓜', 'poll': random.randint(0, 100)},
        {'name': '鳳梨', 'poll': random.randint(0, 100)},
        {'name': '蘋果', 'poll': random.randint(0, 100)},
        {'name': '草莓', 'poll': random.randint(0, 100)}
    ]
    return render(request, 'page_polls.html', locals())


def form_profile(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        age = request.POST['age']
        sex = request.POST['sex']
        email = request.POST['email']
        order = request.POST['order']

    return render(request, 'form_profile.html', locals())


