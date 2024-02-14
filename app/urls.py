from django.urls import path
from app import views

urlpatterns = [
    path('login', views.login, name='login'),
     path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('new-record', views.newRecord, name='newRecord'),
    path('logout', views.signout, name='logout'),
    path('retrieve-record', views.retrieveRecord, name='retrieveRecord')
]