from django.urls import path
from django.conf.urls import url
from .views import profile_view
from . import views
app_name = 'profiles'

urlpatterns = [
    path('', profile_view, name='profile-view'),
    path('panel/', views.panel, name='panel'),
    path('prices/', views.prices, name='prices'),
    path('stock/', views.stock, name='stock'),
    # path('sleep/', test_view_1, name='test-view-1'),
    # path('view3/', test_view_2, name='test-view-2'),
]
