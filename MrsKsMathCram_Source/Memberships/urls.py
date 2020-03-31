from django.urls import path
from .views import MembershipSelectView

app_name = 'Memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
]