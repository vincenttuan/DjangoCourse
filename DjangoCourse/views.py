import datetime
import os
import io
import random

from django.http import HttpResponse
from django.shortcuts import render
from DjangoCourse.form import PostFormModel_Profile
from DjangoCourse.models import Music
from DjangoCourse.twii import twii

from DjangoCourse.models import Music
from DjangoCourse.serializers import MusicSerializer
from rest_framework import viewsets

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
        try:
            order = request.POST['order']
        except:
            order = 'off'
        return render(request, 'form_profile_result.html', locals())
    elif request.method == 'GET':
        return render(request, 'form_profile.html', locals())


def form_profile_model(request):
    if request.method == 'POST':
        postform_model = PostFormModel_Profile(request.POST)
        if postform_model.is_valid():
            username       = postform_model.cleaned_data['username']
            password       = postform_model.cleaned_data['password']
            age            = postform_model.cleaned_data['age']
            sex            = postform_model.cleaned_data['sex']
            email          = postform_model.cleaned_data['email']
            try:
                order      = postform_model.cleaned_data['order']
            except:
                order = 'off'
        return render(request, 'form_profile_result.html', locals())
    elif request.method == 'GET':
        postform_model = PostFormModel_Profile()
        return render(request, 'form_profile_model.html', locals())


def form_twii(request):
    twii_list = []
    if request.method == 'POST':
        r = request.POST['r']
        pe = request.POST['pe']
        pb = request.POST['pb']
        twii_list = twii(float(r), float(pe), float(pb))

    return render(request, 'form_twii.html', locals())


def twii_getcsv(request):
    f = io.open(os.path.join('static/csv', 'BWIBBU_d.csv'), 'r', encoding='utf8')
    data = f.read()
    f.close()
    return HttpResponse(data)


def crud_music(request):
    if request.method == 'POST':
        id = request.POST['id']
        song = request.POST['song']
        singer = request.POST['singer']
        act = request.POST['act']
        if act == '1':
            Music.objects.create(song=song, singer=singer)
        elif act == '2':
            data = Music.objects.filter(id=int(id))
            data.update(song=song, singer=singer)
        elif act == '3':
            data = Music.objects.filter(id=int(id))
            data.delete()

    musics = Music.objects.all()
    return render(request, 'crud_music.html', locals())

def rest_music(request):
    return render(request, 'rest_music.html')

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
