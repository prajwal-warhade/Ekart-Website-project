from django.urls import path
from villageapp import views
from django.conf.urls.static import static
from django.conf import settings #MEDIA_URL is in settings file thats why need to import

urlpatterns = [
     path('products',views.products),
     path('register',views.register),
     path('login',views.user_login),#using inbuild login function user_login.
     path('about',views.about),
     path('contact',views.contact),
     path('logout',views.user_logout),
     path('catfilter/<cp>',views.catfilter),
     path('Product_DE/<pid>',views.Product_DE),
     path('cart/<pid>',views.cart),
     path('viewcart',views.viewcart),
     path('updateqty/<x>/<cid>',views.updateqty),
     path('removecart/<cid>',views.removecart),
     path('placeorder',views.placeorder),
     path('fetchorder',views.fetchorder),
     path('makepayment',views.makepayment),
     path('paysuccess',views.paysuccess),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#this is for image path
