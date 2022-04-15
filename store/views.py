from django.shortcuts import render
from django.views import View
from .models import Product

class ProductView(View):

    def get(self, request, *args, **kwargs):

        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, "products/product_list.html", context)