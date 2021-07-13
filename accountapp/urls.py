from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import code_square, AccountCreateView

app_name = "accountapp"


urlpatterns = [
    path('CODE_SQUARE/', code_square, name='CODE_SQUARE'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name = 'create')
]