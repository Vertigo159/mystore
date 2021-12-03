from django.urls import path
from .views import signin, login_page


urlpatterns = [
    path('signin/', signin, name="signin"),
    path('login/', login_page, name="login")
]