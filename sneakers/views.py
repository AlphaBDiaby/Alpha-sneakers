from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from article.models import Sneaker, Cart, Order


def index(request):
    return render(request,"sneakers/index.html")


def checkout(request):
    return render(request, 'sneakers/checkout.html')


def product_detail(request, slug):
   product = get_object_or_404(Sneaker, slug=slug)
   return render(request, 'article/detail.html', context={"product": product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Sneaker, slug=slug)
    cart, _ =Cart.objects.get_or_create(user=user)
    order, created =Order.objects.get_or_create(user=user,
                                                product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'sneakers/cart.html',context={"orders": cart.orders.all()})
