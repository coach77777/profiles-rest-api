from django.urls import path
from profiles_api import views

app_name = ""
urlpatterns = [
    path('hello-view/' , views.HelloApiView.as_view()),
    
]