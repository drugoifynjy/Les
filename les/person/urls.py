from django.urls import path

from . import views

urlpatterns = [
    path('person_list/', views.PersonView.as_view(), name='person_list'),

    path('person_add/', views.person_add, name='person_add'),
    path('person_mod/<int:pk>/edit', views.person_mod, name='person_mod'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]