# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import CustomUserForm
#
#
# def home(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("User was created successfully.")
#         else:
#             return HttpResponse("There was an error.")
#     else:
#         form = CustomUserForm()
#
#     return render(request, 'registration/home.html', {'form': form})
#
#
#
# #from django.contrib.auth import authenticate, login
# from django.shortcuts import render,redirect
# #from django.contrib.auth.forms import UserCreationForm
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# # Create your views here.
# def indexView(request):
#     return render(request, 'index.html')
#
# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')
#
# @csrf_exempt
# def register(request):
#     form = CustomUserForm(request.POST)
#     if request.method=="POST":
#         if form.is_valid():
#             form.save()
#             return redirect('login_url')
#         else:
#             form=CustomUserForm()
#     return render(request, 'register.html',{'form':form})
#
#
# from rest_framework import viewsets
#
# from .models import CustomUser, ActivityPeriods
# from .serializers import CustomUserSerializer, ActivityPeriodsSerializer
#
#
# class CustomUserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#
#
# class ActivityPeriodsViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     queryset = ActivityPeriods.objects.all()
#     serializer_class = ActivityPeriodsSerializer
#
#

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import simplejson as json
import json

from .models import ActivityPeriods, CustomUser


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


def get_activity(request):
    result = []
    if request.method == 'GET':
        try:
            data = ActivityPeriods.objects.all()
            for i in range(0, len(data)):
                # id=data[i].user.username
                # response = json.dumps([{'id':id}])
                # id=None
                result.append({
                    'id': data[i].user.username,
                    'real_name': data[i].user.real_name,
                    'tz': data[i].user.timezone,
                })

                print(data[i].user.username)
                print(data[i].user.real_name)
                print(data[i].end_time)
            # print(result)

            # obj = {
            #     'username': data.username,
            #     'last_login': data.last_login,
            # }
            # result.append(obj)

        except:
            response = json.dumps([{'Error': 'No Record Found'}])
    return HttpResponse(response, content_type='text/json')

# @csrf_exempt
# def add_car(request):
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         car_name = payload['car_name']
#         top_speed = payload['top_speed']
#         car = Car(name=car_name, top_speed=top_speed)
#         try:
#             car.save()
#             response = json.dumps([{'Success': 'Car added successfully!'}])
#         except:
#             response = json.dumps([{'Error': 'Car could not be added!'}])
#     return HttpResponse(response, content_type='text/json')
