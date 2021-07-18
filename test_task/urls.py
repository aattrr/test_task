from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.MainPage.as_view(), name='main_page'),
    # path('user_for_json/', user_for_json, name='user_for_json'),
    path('export_orders/', export_orders, name='export_orders'),
    path('orders/', include('orders.urls')),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup')
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
