from django.contrib.auth import authenticate, login
from orders.models import Order
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core import serializers
import json


class UserLoginView(LoginView):
    """Вход пользователя"""
    template_name = 'test_task/login.html'
    # success_url = reverse_lazy('main_page')


class UserLogoutView(LogoutView):
    """Выход пользователя"""
    success_url = reverse_lazy('main_page')


class SignUpView(CreateView):
    """Регистрация"""
    form_class = SignUpForm
    template_name = 'test_task/signup.html'
    success_url = reverse_lazy('main_page')
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class MainPage(TemplateView):
    """Главная страница"""
    template_name = "test_task/main.html"


# Экспорт заказов в JSON через базовую авторизацию
# def user_for_json(request, realm="", *args, **kwargs):
#     user = UserForJson.objects.values()
#     username_in_db = user[0]['username']
#     password_in_db = user[0]['password']
#     if request.method == 'POST':
#         form = UserForJsonForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#
#             if "HTTP_AUTHORIZATION" in request.META:
#                 # В заголовке basic-авторизации две части, разделенных пробелом.
#                 auth = request.META["HTTP_AUTHORIZATION"].split()
#                 # Первая — слово "Basic"
#                 if len(auth) == 2 and auth[0].lower() == "basic":
#                     # Затем base64-кодированные имя пользователя и пароль,
#                     # разделенные (после декодирования) двоеточием.
#                     username, password = base64.b64decode(auth[1]).split(":")
#                     # Их и используем с django.contrib.auth.authenticate
#                     user = authenticate(username=username, password=password)
#
#                     # Если не авторизовали — даем ответ с 401, требуем авторизоваться
#                     if user is None or not user.is_active():
#                         response = HttpResponse()
#                         response.status_code = 401
#                         # realm — любое уникальное (в пределах действия имени пользователя и пароля)
#                         # имя, например, "API" или "Private area"
#                         response["WWW-Authenticate"] = 'Basic realm="%s"' % realm
#                         return response
#     else:
#         context = {
#             'form': UserForJsonForm(),
#         }
#         return render(request, 'test_task/export_orders.html', context)


# Экспорт заказов в JSON(data_export.json в корне проекта)
def export_orders(request):
    orders_to_json = serializers.serialize("json", Order.objects.all())
    with open('data_export.json', 'w', encoding='utf-8') as outfile:
        json.dump(orders_to_json, outfile, ensure_ascii=False, indent=4)
    return HttpResponse(orders_to_json, content_type='application/json')
