from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from kitchen.models import Dish, Cook, DishType
from kitchen.forms import CookCreationForm


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
    }

    return render(request, "kitchen/index.html", context=context)


def signup(request):
    if request.method == "POST":
        form = CookCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("kitchen:index")
    else:
        form = CookCreationForm()
    return render(request, "registration/signup.html", {"form": form})
