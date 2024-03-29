from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("book/<str:pk>/", views.book_view, name="book-view"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path("signup/", views.signupView, name="signup"),
    path("myaccount/", views.myaccount, name="myaccount"),
    path("myaccount/edit/", views.edit_myaccount, name="edit_myaccount"),
    path("about/", views.about, name="about"),
]
