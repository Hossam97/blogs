from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context = {"form": form}
    return render(request, "accounts/register.html", context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_auth(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
        context = {"form": form}
    ###################### Another way of login authentication ################
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         login_auth(request, user)
    #         return redirect('/')
    #
    #     else:
    #         context = {
    #             "error": "Invalid username or password!"
    #         }
    #         return render(request, "accounts/login.html", context=context)
    return render(request, "accounts/login.html", context)

def logout(request):
    if request.method == 'POST':
        logout_auth(request)
        return redirect('/login/')
    return render(request, "accounts/logout.html", {})