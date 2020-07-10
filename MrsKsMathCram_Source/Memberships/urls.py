from django.urls import path
from .views import MembershipSelectView, PaymentView, UpdateTransactions, profile_view, cancelSubscription

app_name = 'Memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', UpdateTransactions, name='update-transactions'),
    path('profile/', profile_view, name='profile'),
    path('cancel/', cancelSubscription, name='cancel'),
]