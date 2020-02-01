from django.urls import path
from . import views
from .views import HomeView, get_data, ChartData

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('api/data', get_data, name="api-data"),
    path('api/chart/data', ChartData.as_view(), name="api-chart-data"),
    # path('/index', views.index, name='home-page'),
    # path('buttons', views.buttons, name='button'),
    # path('/login', views.login, name='login'),
    # path('/register', views.register, name='register'),


]