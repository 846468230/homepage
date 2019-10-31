from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('<int:user_id>',views.UserView.as_view(),name="homepage"),
    path('app/<int:user_id>',views.AppView.as_view(),name="apppage"),

]