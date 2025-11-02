from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Category, MenuItem, Topping, Order, OrderItem
from .forms import CheckoutForm
import json

def menu_view(request):
    """Main menu page view"""
    categories = Category.objects.prefetch_related('items').all()
    context = {
        'categories': categories,
    }
    return render(request, 'menu.html', context)

def about(request):
    return render(request, 'about.html')

def checkout_view(request):
    """Checkout page view"""
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        cart_data = request.POST.get('cart_data')
        
        if form.is_valid() and cart_data:
            try:
                cart = json.loads(cart_data)
                
                # Calculate total
                total = sum(item['price'] * item['quantity'] for item in cart)
                
                # Create order
                order = form.save(commit=False)
                order.total = total
                order.status = 'PENDING'
                order.save()
                
                # Create order items
                for item in cart:
                    menu_item = MenuItem.objects.get(id=item['id'])
                    OrderItem.objects.create(
                        order=order,
                        menu_item=menu_item,
                        quantity=item['quantity'],
                        price=item['price']
                    )
                
                # Store order ID in session
                request.session['order_id'] = order.id
                
                return redirect('pizza_menu:order_confirmation')
            except Exception as e:
                messages.error(request, f'Error processing order: {str(e)}')
        else:
            if not cart_data:
                messages.error(request, 'Your cart is empty.')
    else:
        form = CheckoutForm()
    
    context = {
        'form': form,
    }
    return render(request, 'checkout.html', context)

def order_confirmation_view(request):
    """Order confirmation page"""
    order_id = request.session.get('order_id')
    
    if not order_id:
        return redirect('pizza_menu:menu')
    
    order = get_object_or_404(Order, id=order_id)
    
    # Clear the order from session
    if 'order_id' in request.session:
        del request.session['order_id']
    
    context = {
        'order': order,
    }
    return render(request, 'order_confirmation.html', context)

def get_toppings(request):
    """API endpoint to get all available toppings"""
    toppings = Topping.objects.filter(is_available=True)
    toppings_data = {}
    
    for topping in toppings:
        topping_type = topping.topping_type
        if topping_type not in toppings_data:
            toppings_data[topping_type] = []
        toppings_data[topping_type].append({
            'id': topping.id,
            'name': topping.name,
            'calories': topping.calories,
        })
    
    return JsonResponse(toppings_data)

@require_http_methods(["POST"])
def add_to_cart(request):
    """API endpoint to add item to cart"""
    try:
        data = json.loads(request.body)
        # Cart logic would go here - for now, return success
        return JsonResponse({'success': True, 'message': 'Item added to cart'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
