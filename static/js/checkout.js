// Initialize checkout page
document.addEventListener('DOMContentLoaded', function() {
    // Load cart from localStorage
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    
    // If cart is empty, redirect back
    if (cart.length === 0) {
        window.location.href = '/';
        return;
    }
    
    // Populate order summary
    renderOrderSummary(cart);
    
    // Set cart data in hidden field
    document.getElementById('cartData').value = JSON.stringify(cart);
    
    // Handle order type change (show/hide delivery address)
    const orderTypeRadios = document.querySelectorAll('input[name="order_type"]');
    const deliverySection = document.getElementById('deliverySection');
    
    orderTypeRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.value === 'DELIVERY') {
                deliverySection.style.display = 'block';
                document.querySelector('[name="delivery_address"]').required = true;
            } else {
                deliverySection.style.display = 'none';
                document.querySelector('[name="delivery_address"]').required = false;
            }
        });
    });
    
    // Form submission
    const form = document.getElementById('checkoutForm');
    form.addEventListener('submit', function(e) {
        // Form will submit normally, but we clear cart on success
        // Cart will be cleared after redirect to confirmation page
    });
});

function renderOrderSummary(cart) {
    const summaryItemsContainer = document.getElementById('summaryItems');
    
    if (cart.length === 0) {
        summaryItemsContainer.innerHTML = '<p class="empty-summary">Your cart is empty</p>';
        return;
    }
    
    let html = '';
    let subtotal = 0;
    
    cart.forEach(item => {
        const itemTotal = item.price * item.quantity;
        subtotal += itemTotal;
        
        html += `
            <div class="summary-item">
                <div class="summary-item-info">
                    <div class="summary-item-name">${item.name}</div>
                    <div class="summary-item-quantity">Qty: ${item.quantity}</div>
                </div>
                <div class="summary-item-price">$${itemTotal.toFixed(2)}</div>
            </div>
        `;
    });
    
    summaryItemsContainer.innerHTML = html;
    
    // Calculate totals
    const tax = subtotal * 0.08;
    const total = subtotal + tax;
    
    document.getElementById('summarySubtotal').textContent = `$${subtotal.toFixed(2)}`;
    document.getElementById('summaryTax').textContent = `$${tax.toFixed(2)}`;
    document.getElementById('summaryTotal').textContent = `$${total.toFixed(2)}`;
}

