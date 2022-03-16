from django.urls import path

from . import views

urlpatterns = [
    path('persons_list/', views.PersonView.as_view(), name='persons_list'),
    path('person_add/', views.PersonAdd.as_view(), name='person_add'),
    path('person_mod/<int:pk>/edit', views.PersonMod.as_view(), name='person_mod'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]