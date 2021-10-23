from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
    path('', login_required(views.LinkCreate.as_view()), name="home")
]
