# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


from django.shortcuts import render
from .models import Product

def home(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'selected_category': None  # optional if used in template
    })


def product_detail(request, pk):  # ✅ THIS MUST BE "pk" NOT "id"
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})



from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

from .models import Product, Category

def category_filter(request, category_id):
    selected_category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=selected_category)
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    })

from django.shortcuts import get_object_or_404, redirect

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        subtotal = product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
        total += subtotal

    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if quantity > 0:
            cart[str(product_id)] = quantity
        else:
            cart.pop(str(product_id), None)
        request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

from .models import Order
from django.contrib import messages
from django.shortcuts import redirect

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect('home')

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        payment_method = request.POST['payment_method']

        products = Product.objects.filter(id__in=cart.keys())
        total_price = 0
        cart_data = []

        for product in products:
            quantity = cart[str(product.id)]
            subtotal = product.price * quantity
            total_price += subtotal
            cart_data.append({
                'product_id': product.id,
                'name': product.name,
                'price': float(product.price),
                'quantity': quantity,
                'subtotal': float(subtotal)
            })

        order = Order.objects.create(
            name=name,
            address=address,
            payment_method=payment_method,
            cart_data=cart_data,
            total_price=total_price
        )

        request.session['cart'] = {}  # Clear cart
        messages.success(request, f"Order #{order.id} placed successfully!")
        return redirect('home')

    return render(request, 'store/checkout.html')

from django.contrib.auth.decorators import login_required

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})
