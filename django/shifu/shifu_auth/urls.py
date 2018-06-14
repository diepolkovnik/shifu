from django.urls import path, include
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('account/reset-password', password_reset, name='reset_password'),
    path('account/reset-password/done', password_reset_done, name='reset_password_done'),
    path('account/reset-password/confirm', password_reset_confirm, name='password_reset_confirm'),
    path('account/reset-password/complete', password_reset_complete, name='password_reset_complete'),

]
