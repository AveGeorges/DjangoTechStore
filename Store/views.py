from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Product
from django.urls import reverse


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
   quantity = len(Product.objects.all())
   print(quantity)
   if product_id < 1:
      raise Http404()
   elif product_id > quantity:
      return redirect("Store:items")
   product = Product.objects.get(id=product_id)
   context = {
      "item": product
   }
   return render(request=request, template_name="Store/product-info.html", context=context)


def get_work_portfolio(request, work_slug):
   if work_slug == "tgbot":
      return HttpResponse("Это работа №1")
   elif work_slug == "parsing":
      return HttpResponse("Это работа №2")
   else:
      uri = reverse("Store:archive", args=(2023, ))
      return redirect(uri)
   
   
def archive_portfolio(request, year):
   if year > 2025:
      return HttpResponseNotFound("<h1>Страница не найдена</h1>")
   else:
      return HttpResponse(f'Это архивная работа {year} года')


def handle_error_404(request, exception):
   return HttpResponseNotFound("<h1>Страница не найдена</h1>")
