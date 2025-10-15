# Quick Start Guide

Get your DOM Pizza site running in 3 easy steps!

## 🚀 Quick Setup

### Step 1: Install Django
```bash
pip install -r requirements.txt
```

### Step 2: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py load_sample_data
```

### Step 3: Run the Server
```bash
python manage.py runserver
```

Then open your browser to: **http://localhost:8000** 🍕

---

## 🎨 What You'll See

Your pizza ordering site features:

- **Modern Dark Theme** - Sleek design inspired by MOD Pizza
- **8 Menu Categories**:
  - Dinner and a Movie
  - Pizza (with signature pizzas like Mad Dog, Caspian, etc.)
  - Salads
  - Kids Meal
  - Sides (Cheesy Garlic Bread, etc.)
  - Beverages
  - Desserts
  - Extras

- **Interactive Features**:
  - ✅ Working shopping cart
  - ✅ Add/remove items with quantity controls
  - ✅ Cart persists between sessions (localStorage)
  - ✅ Smooth scroll navigation
  - ✅ Responsive mobile design
  - ✅ Beautiful animations

---

## 🛠️ Optional: Create Admin Account

To manage menu items through the admin panel:

```bash
python manage.py createsuperuser
```

Then visit: **http://localhost:8000/admin**

---

## 📱 Features Breakdown

### Header
- Store location selector
- Pickup/delivery toggle
- Sign in button
- Shopping cart with live count

### Navigation
- Sticky menu bar
- Smooth scrolling to sections
- Active section highlighting

### Menu Items
- Cards with hover effects
- "TOP PICK" and "DEAL" tags
- Price and calorie information
- One-click "Add to Cart"

### Shopping Cart Modal
- View all cart items
- Adjust quantities (+/-)
- Remove items
- See total price
- Checkout button

---

## 🎯 What's Included

```
✅ Django backend fully configured
✅ Database models for menu items, categories, orders
✅ Beautiful responsive UI
✅ 30+ sample menu items loaded
✅ 40+ toppings database
✅ Cart functionality with localStorage
✅ Admin panel for easy management
✅ Mobile-friendly design
```

---

## 🔧 Customization

### Change Colors
Edit `static/css/style.css` - look for CSS variables:
```css
:root {
    --primary-red: #e31837;
    --dark-bg: #1a1a1a;
    /* ... */
}
```

### Add Menu Items
Use the admin panel at `/admin` or edit the database directly.

### Add Images
Set the `image` URL field for menu items in admin panel.

---

## 📚 Next Steps

1. ✅ Run the site (you're here!)
2. 🔐 Create admin user
3. 🍕 Customize menu items
4. 🎨 Adjust colors/styling
5. 💳 Add checkout functionality
6. 🚚 Implement order tracking

Enjoy your pizza ordering site! 🍕🎉

