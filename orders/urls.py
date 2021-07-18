from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


urlpatterns = [
    path('', OrderList.as_view(), name='order_list'),
    path('<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('create_order/', login_required(CreateOrder.as_view()), name='create_order'),
    path('<int:pk>/delete_order/', login_required(DeleteOrder.as_view()), name='delete_order'),
]
