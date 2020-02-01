import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context, loader
from django.shortcuts import render
from django.views.generic import View
# for basic query set
from django.contrib.auth import get_user_model


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

User = get_user_model()


# def index(request):
#     template = loader.get_template("./myapp/index.html")
#     return HttpResponse(template.render())
#
#
# def buttons(request):
#     template = loader.get_template("./myapp/buttons.html")
#     return HttpResponse(template.render())
#
#
# def login(request):
#     template = loader.get_template("./myapp/login.html")
#     return HttpResponse(template.render())\
#
#
# def register(request):
#     template = loader.get_template("./myapp/register.html")
#     return HttpResponse(template.render())
#
# # three ways of passing data to website but using rest fraamework is the preferred way of doing it

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'charts.html',{"customers": 20})

def get_data(request, *args, **kwargs):
    data={
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) #http response
#
# def get_json(request, *args, **kwargs):
#     data = json.load(open('preddata.json'))
#     return Response(data) #http response

# for trying out chart.js using in built generic views
class ChartData(APIView):

    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        #
        # with open('./preddata.json','r') as f:
        #     default_items=json.loads(f)

        return Response('It worked')
