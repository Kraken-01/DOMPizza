from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    ITEM_TAGS = [
        ('', 'None'),
        ('TOP_PICK', 'Top Pick'),
        ('DEAL', 'Deal'),
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.CharField(max_length=50, blank=True)
    image = models.URLField(blank=True)
    tag = models.CharField(max_length=20, choices=ITEM_TAGS, blank=True)
    is_signature = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Topping(models.Model):
    TOPPING_TYPES = [
        ('SAUCE', 'Sauce'),
        ('CHEESE', 'Cheese'),
        ('MEAT', 'Meat'),
        ('VEGGIE', 'Vegetable'),
        ('FINISH', 'Finishing Sauce'),
    ]
    
    name = models.CharField(max_length=100)
    topping_type = models.CharField(max_length=20, choices=TOPPING_TYPES)
    calories = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['topping_type', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_topping_type_display()})"

class Order(models.Model):
    ORDER_STATUS = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready for Pickup'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    order_type = models.CharField(max_length=20, choices=[('PICKUP', 'Pickup'), ('DELIVERY', 'Delivery')])
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='PENDING')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    special_instructions = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name}"

class OrderItemTopping(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='toppings')
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.topping.name}"

