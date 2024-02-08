from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    # path("login/", auth_views.LoginView.as_view(template_name="products/login.html", authentication_form=LoginForm), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("detail/<int:pk>/", views.detail, name='detail'),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("new/", views.new_item, name="new_item"),
    path("edit/<int:pk>/", views.edit_item, name="edit_item"),
    path("search/", views.search, name="search"),

]
