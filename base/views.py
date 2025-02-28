from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import json
import random
import numpy as np
import pandas as pd
import pickle
# from PIL import Image
# from torchvision import transforms
# from sklearn.feature_extraction.text import TfidfVectorizer








# Home page view
def HomePage(request):
    return render(request, 'home.html')


# Signup view
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


# Login view
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!")

    return render(request, 'login.html')


# Logout view
def LogoutPage(request):
    logout(request)
    return redirect('home')

def getPredictions(a, b, c, d, e, f, g):
    model = pickle.load(open('Models\\KNN.pkl', 'rb'))
    prediction = model.predict(np.array([[a, b, c, d, e, f, g]]))
    return prediction[0]

@login_required(login_url='login')
def result(request):
    a = eval(request.GET['N'])
    b = eval(request.GET['P'])
    c = eval(request.GET['K'])
    d = eval(request.GET['temperature'])
    e = eval(request.GET['humidity'])
    f = eval(request.GET['ph'])
    g = eval(request.GET['rainfall'])
    result = getPredictions(a, b, c, d, e, f, g)
    return render(request, 'result.html', {'result': result})



def getPredictions3(a, b, c, d, e):
    model = pickle.load(open('Models\\Weather_Rf.pkl', 'rb'))
    new_data = {
            'date': a,
            'precipitation':b,
           'temp_max':c,
            'temp_min':d,
           'wind':e
           }
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return prediction[0]

@login_required(login_url='login')
def result3(request):
    a = str(request.GET['date'])
    b = float(request.GET['precipitation'])
    c = float(request.GET['temp_max'])
    d = float(request.GET['temp_min'])
    e = float(request.GET['wind'])
    result = getPredictions3(a, b, c, d, e)
    return render(request, 'result3.html', {'result': result})



# Additional views
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def index3(request):
    return render(request, 'index3.html')
