from django.urls import path
from . import views
from .views import handle_error_404


app_name = 'Store'

urlpatterns = [
    path("", view=views.index, name='main'),
    path("products/", view=views.get_products, name="items"),
    path("products/<int:product_id>/", view=views.get_product, name="item"),
    
    path("portfolio/<slug:work_slug>/", view=views.get_work_portfolio, name="work"),
    path("archive-portfolio/<int:year>/", view=views.archive_portfolio, name="archive")
]



