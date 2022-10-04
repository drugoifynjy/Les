from django.urls import path
from .views import *

urlpatterns = [
    path('guides/organizations/', OrganizationsView.as_view(), name='organizations_list'),
    path('guides/organizations/organization_mod/<int:pk>', OrganizationAddOrMod.as_view(), name='organization_mod'),
    path('guides/organizations/<int:dep_pk>/representatives/', RepresentativeList.as_view(), name='representatives_list'),
    path('guides/organizations/<int:dep_pk>/representative_mod/<int:pk>', RepresentativeAddOrMod.as_view(), name='representative_mod'),
    path('guides/organizations/<int:org_pk>/bank_details_list/', BankDetailsList.as_view(), name='bank_details_list'),
    path('guides/organizations/<int:org_pk>/bank_details_mod/<int:pk>', BankDetailsAddOrMod.as_view(), name='bank_details_mod'),
    path('guides/organizations/<int:org_pk>/departments_list/', DepartmentList.as_view(), name='departments_list'),
    path('guides/organizations/<int:org_pk>/department_mod/<int:pk>', DepartmentAddOrMod.as_view(), name='department_mod'),
]
