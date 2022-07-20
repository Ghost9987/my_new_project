from django.shortcuts import render
from hello.views import TotalPriceView 

# Create your views here.

class MyView(view):
    def get(self, request, *args, **kwargs):
        data = [{
            "name": item.name,
            "price": item.price
        } for item in item.objects.all()]
        return HTTPResponse(data)

class TotalPriceView(View):
    def get(self, request, *args, **kwargs):
        total_price = sum([item.price for item in item.objects.all()])
        return HttpResponse(f"the total price for all items is {total.price}")