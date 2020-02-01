import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context, loader
from django.shortcuts import render
from django.views.generic import View
# for basic query set
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

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
class ChartData(BaseLineChartView):
    ## -- Process your data here!
    ## I'm guessing you want to use a line graph? I used a line graph here.
    ## Note, get the data first from somewhere.
    ## https://github.com/peopledoc/django-chartjs
    ## That was for charts

    ## https://pypi.org/project/requests/

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""
        ## Opening a file example
        with open('./test1.json') as f:
            x = f.read()
            print(x)

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = ChartData.as_view()