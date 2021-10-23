from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from dashboard.models import Link
# Create your views here.


def home(request, username):
    user = get_object_or_404(User, username=username)
    links = Link.objects.filter(owner=user)

    return render(request, 'front/home.html', {'user': user, 'links': links})
