"""mini_commerce URL Configuration"""


from django.contrib import admin
from django.urls import path
from products.views import list_products
from payment.views import pay_products, confirm_pay, list_trans, confirm_delivery, make_order, revert_order
from users.views import login_view, log_out, sign_up
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("list_products/", list_products, name="list_products"),
    path("make_order/", make_order, name="make_order"),
    path("confirm_pay/<str:order_token>", confirm_pay, name="confirm_pay"),
    path("list_trans/", list_trans.as_view(), name="list_trans"),
    path("confirm_delivery/<str:order_token>", confirm_delivery, name="confirm_delivery"),
    path("", login_view, name="login_view"),
    path("log_out/", log_out, name="log_out"),
    path("sign_up/", sign_up, name="sign_up"),
    path("pay_products/<int:pk>", pay_products.as_view(), name="pay_products"),
    path("revert_order/", revert_order, name="revert_order")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
