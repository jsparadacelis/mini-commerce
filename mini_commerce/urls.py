"""mini_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import list_products
from payment.views import detail_products, pay_products, order_by, confirm_pay, list_trans, confirm_delivery

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", list_products, name="list_products"),
    path("detail_products/", detail_products, name="detail_products"),
    path("pay_products/", pay_products, name="pay_products"),
    path("order_by/<int:id>", order_by, name="order_by"),
    path("confirm_pay/<str:order_token>", confirm_pay, name="confirm_pay"),
    path("list_trans/", list_trans, name="list_trans"),
    path("confirm_delivery/<str:order_token>", confirm_delivery, name="confirm_delivery"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
