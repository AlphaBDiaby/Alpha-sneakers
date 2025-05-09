from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def cart(request):
    cart_items = request.session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def checkout(request):
    return render(request, 'checkout.html')


