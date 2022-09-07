from django.urls import path
from .views import *

urlpatterns = [
    path('guides/locality_type/', LocalityTypesList.as_view(), name='locality_types_list'),
    path('guides/locality_type/locality_type_mod/<int:pk>', LocalityTypeAddOrMod.as_view(), name='locality_type_mod'),

    path('persons_list/', PersonView.as_view(), name='persons_list'),
    path('person_add/', PersonAdd.as_view(), name='person_add'),
    path('person_mod/<int:pk>/edit', PersonMod.as_view(), name='person_mod'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]
