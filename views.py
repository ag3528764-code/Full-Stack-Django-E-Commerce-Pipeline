from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Product, Order

def product_list(request):
    # This automatically adds products to your database if it's completely empty
    if not Product.objects.exists():
        Product.objects.create(
            name="Premium Mechanical Keyboard",
            description="Tactile blue switches, custom RGB backlit profile, aluminum frame design perfect for intensive development.",
            price=129.99,
            image_url="https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=600"
        )
        Product.objects.create(
            name="Ergonomic Wireless Mouse",
            description="High precision tracking engine with ultra-comfortable side grips designed for endless workspace hours.",
            price=79.50,
            image_url="https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=600"
        )

    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
        'stripe_key': settings.STRIPE_PUBLIC_KEY,
        'razorpay_key': settings.RAZORPAY_KEY_ID
    }
    return render(request, 'store/checkout.html', context)

def process_payment(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        provider = request.POST.get('provider', 'STRIPE')
        
        # Saves the purchase record directly into your SQLite database
        order = Order.objects.create(
            product=product,
            payment_provider=provider,
            status='COMPLETED'
        )
        return render(request, 'store/success.html', {'order': order})
        
    return redirect('product_list')