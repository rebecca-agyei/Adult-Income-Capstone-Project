from django.urls import path, include
from . import views


urlpatterns = [
    # path("", views.home, name='home'),
    path("", views.PredictCreate, name="home"),
    path("predictlist/", views.PredictList.as_view(), name="predict_list"),
    path("account/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.logout_view, name="logout"),
]