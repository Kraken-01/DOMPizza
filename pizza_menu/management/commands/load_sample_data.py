from django.core.management.base import BaseCommand
from pizza_menu.models import Category, MenuItem, Topping

class Command(BaseCommand):
    help = 'Load sample menu data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading sample data...')
        
        # Clear existing data
        MenuItem.objects.all().delete()
        Category.objects.all().delete()
        Topping.objects.all().delete()
        
        # Create Categories
        categories = [
            {'name': 'Din and a Movie', 'description': 'combo meals for your evening', 'order': 1},
            {'name': 'Pizza', 'description': 'Create Your Own With Unlimited Toppings...Or Save Some $$ With Our Everyday Pizza Deals...Or Customize One Of Our Signature Pizzas', 'order': 2},
            {'name': 'Salads', 'description': 'Create Your Own With Unlimited Toppings, Or Customize One Of Our Signature Salads', 'order': 3},
            {'name': 'Kids Meal', 'description': 'Because parents shouldn\'t have to share their pizza', 'order': 4},
            {'name': 'Sides', 'description': 'Round out your meal with something on the side', 'order': 5},
            {'name': 'Beverages', 'description': '', 'order': 6},
            {'name': 'Desserts', 'description': '', 'order': 7},
            {'name': 'Extras', 'description': '', 'order': 8},
        ]
        
        for cat_data in categories:
            Category.objects.create(**cat_data)
        
        # Create Menu Items
        menu_items = [
            # Dinner and a Movie
            {
                'category': 'Dinner and a Movie',
                'name': 'Pizza for 2 Combo',
                'description': 'Customize two MOD-sized pizzas with unlimited toppings for one price. Choose from over 40 toppings and 8 finishing sauces! Includes your choice of two 20oz Coca-Cola bottled beverages.',
                'price': 29.99,
                'calories': '',
                'tag': '',
                'order': 1
            },
            {
                'category': 'Dinner and a Movie',
                'name': 'Salad for 2 Combo',
                'description': 'Customize two MOD-sized salads with unlimited toppings for one price. Choose from over 40 toppings and 8 salad dressings! Includes your choice of two 20oz Coca-Cola bottled beverages.',
                'price': 24.99,
                'calories': '',
                'tag': '',
                'order': 2
            },
            {
                'category': 'Dinner and a Movie',
                'name': 'Mega Cookie',
                'description': 'Sliced into 6 big pieces, the warm and gooey chocolatey Mega Cookie is perfect to share (or not)!',
                'price': 6.99,
                'calories': '1610 Cals',
                'tag': '',
                'order': 3
            },
            
            # Pizza
            {
                'category': 'Pizza',
                'name': 'Unlimited Toppings',
                'description': 'Create your own pizza from over 40 toppings and 8 finishing sauces - and it\'s always unlimited toppings, one price',
                'price': 11.99,
                'calories': '',
                'tag': 'TOP_PICK',
                'order': 1
            },
            {
                'category': 'Pizza',
                'name': 'One Topping',
                'description': 'Keep it simple! Comes with sauce and cheese, plus add your favorite single topping',
                'price': 8.99,
                'calories': '',
                'tag': 'DEAL',
                'order': 2
            },
            {
                'category': 'Pizza',
                'name': 'Cheese (The Maddy)',
                'description': 'Our starter pizza, at a special price! Includes sauce and cheese',
                'price': 7.99,
                'calories': '',
                'tag': 'DEAL',
                'order': 3
            },
            {
                'category': 'Pizza',
                'name': 'Mad Dog',
                'description': 'Signature Tomato Sauce, Mozzarella, Pepperoni, Mild Italian Sausage, Seasoned Ground Beef',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 4
            },
            {
                'category': 'Pizza',
                'name': 'Caspian',
                'description': 'Sweet BBQ Sauce, Mozzarella, Gorgonzola, Grilled Chicken, Sliced Red Onions, Sweet BBQ Finish',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 5
            },
            {
                'category': 'Pizza',
                'name': 'Dillon James',
                'description': 'Signature Tomato Sauce, Chopped Garlic, Fresh Chopped Basil, Mozzarella, Asiago, Vine-ripened Tomatoes',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 6
            },
            {
                'category': 'Pizza',
                'name': 'Jasper',
                'description': 'Signature Tomato Sauce, Mozzarella, Spicy Chicken Sausage, Mushrooms',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 7
            },
            {
                'category': 'Pizza',
                'name': 'Calexico',
                'description': 'Signature Tomato Sauce, Mozzarella, Gorgonzola, Grilled Chicken, Pickled Jalapeños, Spicy Buffalo Finish',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 8
            },
            {
                'category': 'Pizza',
                'name': 'Tristan',
                'description': 'Mozzarella, Asiago, Mushrooms, Roasted Red Peppers, Garlic Pesto Finish',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 9
            },
            {
                'category': 'Pizza',
                'name': 'Dominic',
                'description': 'Creamy Alfredo Sauce, Fresh Chopped Basil, Asiago, Mild Italian Sausage, Sliced Red Onions, Vine-ripened Tomatoes',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 10
            },
            {
                'category': 'Pizza',
                'name': 'Lucy Sunshine',
                'description': 'Garlic Rub, Mozzarella, Aged Parmesan, Artichokes, Signature Tomato Sauce Dollops',
                'price': 11.99,
                'calories': '',
                'tag': '',
                'is_signature': True,
                'order': 11
            },
            
            # Salads
            {
                'category': 'Salads',
                'name': 'Unlimited Toppings',
                'description': 'Create your own salad from over 40 toppings and 8 salad dressings - and it\'s always unlimited toppings, one price',
                'price': 10.99,
                'calories': '',
                'tag': 'TOP_PICK',
                'order': 1
            },
            {
                'category': 'Salads',
                'name': 'Garden',
                'description': 'Romaine, Mixed Spring Greens, Vine-ripened Tomatoes, Diced Cucumbers, Sherry Dijon Vinaigrette',
                'price': 10.99,
                'calories': '',
                'tag': '',
                'order': 2
            },
            {
                'category': 'Salads',
                'name': 'Caesar',
                'description': 'Romaine, Asiago, Aged Parmesan, Croutons, Caesar Dressing',
                'price': 10.99,
                'calories': '',
                'tag': '',
                'order': 3
            },
            {
                'category': 'Salads',
                'name': 'Greek',
                'description': 'Romaine, Feta, Sliced Red Onions, Black Olives, Mama Lil\'s Sweet Hot Peppas, Vine-ripened Tomatoes, Diced Cucumbers, Chickpeas, Greek Vinaigrette',
                'price': 10.99,
                'calories': '',
                'tag': '',
                'order': 4
            },
            {
                'category': 'Salads',
                'name': 'Italian Chop',
                'description': 'Romaine, Arugula, Mozzarella, Aged Parmesan, Genoa Salami, Sliced Red Onions, Black Olives, Chickpeas, Green Bell Peppers, Zesty Tomato Vinaigrette',
                'price': 10.99,
                'calories': '',
                'tag': '',
                'order': 5
            },
            
            # Kids Meal
            {
                'category': 'Kids Meal',
                'name': 'Kids Meal',
                'description': 'A Mini (6") cheese or pepperoni pizza + beverage. (No modifications or substitutions)',
                'price': 6.99,
                'calories': '',
                'tag': '',
                'order': 1
            },
            
            # Sides
            {
                'category': 'Sides',
                'name': 'Cheesy Garlic Bread',
                'description': 'An 11-inch thick crust, covered in garlic and baked to perfection with mozzarella and parmesan. This shareable side is topped with fresh rosemary and ready for dipping.',
                'price': 7.79,
                'calories': '1340 Cals',
                'tag': '',
                'order': 1
            },
            {
                'category': 'Sides',
                'name': 'Side Caesar',
                'description': 'Complete your meal! Romaine, parmesan, asiago, croutons, Caesar dressing. (No modifications or substitutions)',
                'price': 6.89,
                'calories': '410 Cals',
                'tag': 'DEAL',
                'order': 2
            },
            {
                'category': 'Sides',
                'name': 'Side Garden',
                'description': 'Complete your meal! Mixed greens, romaine, diced tomatoes, cucumbers, sherry dijon vinaigrette dressing. (No modifications or substitutions)',
                'price': 6.89,
                'calories': '140 Cals',
                'tag': 'DEAL',
                'order': 3
            },
            
            # Beverages
            {
                'category': 'Beverages',
                'name': 'Fountain Drink (16 oz)',
                'description': 'House-made iced teas and lemonades, Coca-Cola® and Dr Pepper™ sodas - PICKUP ONLY',
                'price': 3.19,
                'calories': '0-320 Cals',
                'tag': '',
                'order': 1
            },
            {
                'category': 'Beverages',
                'name': 'Fountain Drink (24 oz)',
                'description': 'House-made iced teas and lemonades, Coca-Cola® and Dr Pepper™ sodas - PICKUP ONLY',
                'price': 3.49,
                'calories': '0-480 Cals',
                'tag': '',
                'order': 2
            },
            {
                'category': 'Beverages',
                'name': 'Coke Classic (20 oz bottle)',
                'description': '',
                'price': 3.79,
                'calories': '240 Cals',
                'tag': '',
                'order': 3
            },
            {
                'category': 'Beverages',
                'name': 'Diet Coke (20 oz bottle)',
                'description': '',
                'price': 3.79,
                'calories': '0 Cals',
                'tag': '',
                'order': 4
            },
            {
                'category': 'Beverages',
                'name': 'Sprite (20 oz bottle)',
                'description': '',
                'price': 3.79,
                'calories': '230 Cals',
                'tag': '',
                'order': 5
            },
            {
                'category': 'Beverages',
                'name': 'Water (16.9 oz bottle)',
                'description': '',
                'price': 2.29,
                'calories': '0 Cals',
                'tag': '',
                'order': 6
            },
            
            # Desserts
            {
                'category': 'Desserts',
                'name': 'Mega Cookie',
                'description': 'Sliced into 6 big pieces, the warm and gooey chocolatey Mega Cookie is perfect to share (or not)!',
                'price': 6.99,
                'calories': '1610 Cals',
                'tag': '',
                'order': 1
            },
            {
                'category': 'Desserts',
                'name': 'No Name Cake',
                'description': 'A chocolate cake with rich vanilla buttercream center, covered with chocolaty glaze.',
                'price': 3.59,
                'calories': '290 Cals',
                'tag': '',
                'order': 2
            },
            
            # Extras
            {
                'category': 'Extras',
                'name': 'Red Pepper Flakes Packet',
                'description': '',
                'price': 0.00,
                'calories': '0 Cals',
                'tag': '',
                'order': 1
            },
            {
                'category': 'Extras',
                'name': 'Parmesan Cheese Packet',
                'description': '',
                'price': 0.00,
                'calories': '15 Cals',
                'tag': '',
                'order': 2
            },
            {
                'category': 'Extras',
                'name': 'Salt Packet',
                'description': '',
                'price': 0.00,
                'calories': '0 Cals',
                'tag': '',
                'order': 3
            },
            {
                'category': 'Extras',
                'name': 'Pepper Packet',
                'description': '',
                'price': 0.00,
                'calories': '0 Cals',
                'tag': '',
                'order': 4
            },
        ]
        
        for item_data in menu_items:
            category_name = item_data.pop('category')
            category = Category.objects.get(name=category_name)
            MenuItem.objects.create(category=category, **item_data)
        
        # Create Toppings
        toppings = [
            # Sauces
            {'name': 'Signature Tomato Sauce', 'topping_type': 'SAUCE', 'calories': 20},
            {'name': 'Sweet BBQ Sauce', 'topping_type': 'SAUCE', 'calories': 35},
            {'name': 'Creamy Alfredo Sauce', 'topping_type': 'SAUCE', 'calories': 45},
            {'name': 'Garlic Rub', 'topping_type': 'SAUCE', 'calories': 10},
            {'name': 'Olive Oil Drizzle', 'topping_type': 'SAUCE', 'calories': 40},
            
            # Cheese
            {'name': 'Mozzarella', 'topping_type': 'CHEESE', 'calories': 50},
            {'name': 'Asiago', 'topping_type': 'CHEESE', 'calories': 45},
            {'name': 'Aged Parmesan', 'topping_type': 'CHEESE', 'calories': 40},
            {'name': 'Gorgonzola', 'topping_type': 'CHEESE', 'calories': 55},
            {'name': 'Feta', 'topping_type': 'CHEESE', 'calories': 45},
            
            # Meats
            {'name': 'Pepperoni', 'topping_type': 'MEAT', 'calories': 60},
            {'name': 'Mild Italian Sausage', 'topping_type': 'MEAT', 'calories': 70},
            {'name': 'Spicy Chicken Sausage', 'topping_type': 'MEAT', 'calories': 55},
            {'name': 'Grilled Chicken', 'topping_type': 'MEAT', 'calories': 50},
            {'name': 'Seasoned Ground Beef', 'topping_type': 'MEAT', 'calories': 65},
            {'name': 'Genoa Salami', 'topping_type': 'MEAT', 'calories': 60},
            {'name': 'Bacon', 'topping_type': 'MEAT', 'calories': 70},
            {'name': 'Canadian Bacon', 'topping_type': 'MEAT', 'calories': 35},
            
            # Veggies
            {'name': 'Mushrooms', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Sliced Red Onions', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Black Olives', 'topping_type': 'VEGGIE', 'calories': 10},
            {'name': 'Green Bell Peppers', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Roasted Red Peppers', 'topping_type': 'VEGGIE', 'calories': 10},
            {'name': 'Pickled Jalapeños', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Vine-ripened Tomatoes', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Artichokes', 'topping_type': 'VEGGIE', 'calories': 10},
            {'name': 'Fresh Chopped Basil', 'topping_type': 'VEGGIE', 'calories': 0},
            {'name': 'Chopped Garlic', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Spinach', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Arugula', 'topping_type': 'VEGGIE', 'calories': 5},
            {'name': 'Pineapple', 'topping_type': 'VEGGIE', 'calories': 15},
            {'name': 'Chickpeas', 'topping_type': 'VEGGIE', 'calories': 35},
            {'name': 'Diced Cucumbers', 'topping_type': 'VEGGIE', 'calories': 5},
            
            # Finishing Sauces
            {'name': 'Sweet BBQ Finish', 'topping_type': 'FINISH', 'calories': 20},
            {'name': 'Spicy Buffalo Finish', 'topping_type': 'FINISH', 'calories': 25},
            {'name': 'Garlic Pesto Finish', 'topping_type': 'FINISH', 'calories': 40},
            {'name': 'Balsamic Glaze', 'topping_type': 'FINISH', 'calories': 15},
            {'name': 'Ranch Drizzle', 'topping_type': 'FINISH', 'calories': 45},
            {'name': 'Hot Buffalo Sauce', 'topping_type': 'FINISH', 'calories': 10},
        ]
        
        for topping_data in toppings:
            Topping.objects.create(**topping_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data!'))
        self.stdout.write(f'Created {Category.objects.count()} categories')
        self.stdout.write(f'Created {MenuItem.objects.count()} menu items')
        self.stdout.write(f'Created {Topping.objects.count()} toppings')

