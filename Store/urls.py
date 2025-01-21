from django.urls import path
from . import views


app_name = 'Store'

urlpatterns = [
    path("", view=views.index, name='main'),
    path("products/", view=views.get_products, name="items"),
    path("products/<int:product_id>", view=views.get_product, name="item")
]