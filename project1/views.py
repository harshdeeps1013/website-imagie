from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect, reverse, redirect
import logging
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import DocumentForm,CustomUserCreationForm
from django.contrib import messages
import os
from project1.models import image_data,Document
from django.http import JsonResponse
import json
import requests
from django.db.models import F
from django.contrib.auth.models import User

def index(request):
    template_name = 'index.html'

    return render(request, template_name)


def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            user=f.save()
            login(request, user)
            return redirect("home")
    else:
        f = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': f})

def home(request):
    no = []
    im = []
    kk=[]
    photo = image_data.objects.all()
    for pp in photo:
        no.append(pp.name)
        im.append(pp.image_id)
        kk.append(pp.likes)
    lo1 = ["images/" + s for s in no]
    fi = zip(lo1, im,kk)
    ll = {'fin': fi}
    return render(request, 'home.html', ll)

def top_photos(request):
    no = []
    im = []
    kk=[]
    photo=image_data.objects.all().order_by('-likes')

    for pp in photo:
        no.append(pp.name)
        im.append(pp.image_id)
        kk.append(pp.likes)

    lo1 = ["images/" + s for s in no]
    fi = zip(lo1, im,kk)
    ll = {'fin': fi}
    return render(request, 'home.html', ll)


def search(request):
    if request.method=='GET':
        logger = logging.getLogger("mylogger")
        no = []
        im = []
        kk=[]
        altt = request.GET.get('search_d')
        phot=image_data.objects.all()
        photo=phot.filter(name__contains=altt)
        for pp in photo:
            no.append(pp.name)
            logger.info(pp.name)
            im.append(pp.image_id)
            kk.append(pp.likes)
        #logger.info(phot)
        lo1 = ["images/" + s for s in no]
        fi = zip(lo1, im,kk)
        ll = {'fin': fi}
        return render(request, 'home.html', ll)


def logout_request(request):
    logout(request)
    return redirect('home')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


def liker(request):
    logger = logging.getLogger("mylogger")
    if request.method == 'GET':
        logger.info("first_if")
        if request.user.is_authenticated:
            received_data=request.GET.get('photo_id')
            ac=request.GET.get('ac')
            if ac=='inc':
                image_data.objects.filter(image_id=received_data).update(likes=F('likes') + 1)
            elif ac=='dec':
                image_data.objects.filter(image_id=received_data).update(likes=F('likes') - 1)

            logger.info(image_data.objects.filter(image_id=received_data).values())
            data = {'is_done': True}
            return JsonResponse(data)
        else:
            data = {'is_done': False}
            return JsonResponse(data)
    else:
        return HttpResponse("NOT VALID")


def upp(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if form.is_valid():
                altt = form.cleaned_data.get('description')
                nam = request.FILES['image'].name
                use = request.user
                q = image_data(name=nam, submitted_by=use, alt=altt)
                q.save()
                form.save()
                return redirect('home')
        else:
            form = DocumentForm()
            return render(request, 'upload.html', {'form': form})
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})
