from django.urls import path, include
from django.contrib.auth import urls
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("classlist/", views.classlist, name="classlist"),
    path("register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("createposts/", views.createpost, name="post-create"),
    path("blog/id=<int:user_id>/", include([
        path("", views.userblog, name="user-blog"),
        path("<slug:slug>/", views.postdetail, name="post-detail"),
        path("update/<slug:slug>/", views.updatepost, name="update-post"),
        path("delete/<slug:slug>/", views.deletepost, name="delete-post"),
    ])),

   
    

    #path("login/", auth_view.LoginView.as_view(), name="login"),
    #path("logout/", auth_view.LogoutView.as_view(), name="logout"),

]
