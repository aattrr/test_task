from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from orders.models import Order
from .forms import CreateOrderForm


class OrderList(ListView):
    """ Вывод списка книг """
    model = Order
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['order_form'] = CreateOrderForm()
        return context


class OrderDetail(DetailView):
    """Вывод страницы детального описания заказа"""
    model = Order


class CreateOrder(CreateView):
    """Создание заказа"""
    model = Order
    form_class = CreateOrderForm
    # template_name = 'orders/order_list.html'
    success_url = reverse_lazy('order_list')


class DeleteOrder(DeleteView):
    """Удаление заказа"""
    model = Order
    success_url = reverse_lazy('order_list')
