from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import SignupForm
from .models import Book, Category


# Create your views here.
def home(request):
    books = Book.objects.all()[0:3]
    context = {"books": books}
    return render(request, "core/frontpage.html", context)


def shop(request):
    books = Book.objects.all()

    query = request.GET.get("query", "")
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(categories__name__icontains=query)
        ).distinct()
    context = {"books": books}
    return render(request, "core/shop.html", context)


@login_required(login_url="login")
def book_view(request, pk):
    book = Book.objects.get(id=pk)
    context = {"book": book}
    return render(request, "core/book-view.html", context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usename or password incorrect")

    return render(request, "core/login.html")


@login_required(login_url="login")
def logoutView(requet):
    logout(requet)
    return redirect("home")


def signupView(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("home")
        else:
            form = SignupForm()

    return render(request, "core/signup.html")


@login_required(login_url="login")
def myaccount(request):
    return render(request, "core/myaccount.html")


@login_required(login_url="login")
def edit_myaccount(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()

        return redirect("myaccount")
    return render(request, "core/edit_myaccount.html")
