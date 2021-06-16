from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def ulogreg(request):
    if request.method == "POST":
        if request.POST["register"] == "true":
            User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            return JsonResponse({"message": "Your account was successfully created.", "color": "green",
                                 "refresh": "false"}, safe=False)
        else:
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user is None:
                return JsonResponse({"message": "Wrong credentials!", "color": "red", "refresh": "false"}, safe=False)
            else:
                login(request, user)
                return JsonResponse({"message": "You was successfully logged in! You now will be redirected...",
                                     "color": "green", "refresh": "true"}, safe=False)

@login_required
def ulogout(request):
    if request.method == "POST":
        logout(request)
        return redirect("land")
