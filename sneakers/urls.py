from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import signup, logout_user, login_user
from sneakers.views import index, cart, checkout, product_detail, add_to_cart, delete_cart

from sneakers import settings

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('signup/',signup, name="signup" ),
    path('logout/',logout_user, name="logout" ),
    path('login/',login_user, name="login"),
    path('product/<str:slug>/', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('', include('article.urls')),
    path('panier/', cart, name='cart'),
    path('panier/supprimer/', delete_cart, name='delete-cart'),
    path('checkout/', checkout, name='checkout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
