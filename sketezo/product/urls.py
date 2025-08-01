from django.urls import path

from .views import (purchase_clothes_skatezo)

urlpatterns=[
    path('purchase_clothes_skatezo/',purchase_clothes_skatezo, name='purchase_clothes_skatezo'),
]