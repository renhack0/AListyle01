from django.urls import path
from .views import *

urlpatterns = [
    path('savat/', ShoppingcardView.as_view()),
    path('orders/', ProfilOrders.as_view()),
    path('wishlist/', ProfilTanlangan.as_view()),
    path('wishlist_ochir/<int:son>/', WishOchir.as_view()),
    path('item_delete/<int:son>/', SavatItemOchir.as_view()),
    path('tanlangan_qosh/<int:son>/', TanlanganQosh.as_view()),
    path('savat_q/<int:pk>/', MiqdorQosh.as_view()),
    path('savat_k/<int:pk>/', MiqdorKamaytir.as_view()),
    path('item_qosh/<int:pk>/', SavatItemQosh.as_view()),
    path('wishlist_qosh/<int:son>/', TanlanganQosh.as_view()),
]
