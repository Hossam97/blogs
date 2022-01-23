from django.shortcuts import render
from django.http import response
from app.models import Articles
from django.template.loader import render_to_string
import random


# Create your views here.
def home(request):
    context = {}
    if request.method == "GET":
        print(request.user.username)
        articles = Articles.objects.all()
        context['articles'] = articles

    return render(request, "home-view.html", context=context)
