from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(requset):
   return render(request=requset, template_name="Store/index.html")


def get_products(request):
   products = Product.objects.all()
   context = {
      "items": products
   }
   return render(request, template_name="Store/products.html", context=context)


def get_product(request, product_id):
   product = Product.objects.get(id=product_id)
   context = {
      "item": product
   }
   return render(request=request, template_name="Store/product-info.html", context=context)