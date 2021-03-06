from django.urls import path
from .views.payment_views import pay_products, confirm_pay, list_trans, confirm_delivery, make_order, revert_order
from .views.product_views import list_products
from .views.users_views import login_view, log_out, sign_up


urlpatterns = [
    path("list_products/", list_products, name="list_products"),
    path("make_order/", make_order, name="make_order"),
    path("confirm_pay/<slug:order_token>", confirm_pay.as_view(), name="confirm_pay"),
    path("list_trans/", list_trans.as_view(), name="list_trans"),
    path("confirm_delivery/<str:order_token>", confirm_delivery, name="confirm_delivery"),
    path("", login_view, name="login_view"),
    path("log_out/", log_out, name="log_out"),
    path("sign_up/", sign_up, name="sign_up"),
    path("pay_products/<int:pk>", pay_products.as_view(), name="pay_products"),
    path("revert_order/", revert_order, name="revert_order")
    
]