from django.shortcuts import render

# Create your views here.

def purchase_clothes_skatezo(request):
    return render(request,'product/list_products/products_list.html')