# DOM Pizza Ordering Site

A modern, beautiful pizza ordering website built with Django, inspired by MOD Pizza's design.

## Features

- 🍕 Beautiful, responsive menu display
- 🛒 Interactive shopping cart with localStorage persistence
- 📱 Mobile-friendly design
- 🎨 Modern dark theme UI
- ⚡ Smooth animations and transitions
- 📦 Multiple menu categories (Pizza, Salads, Sides, Beverages, Desserts)
- 🏷️ Special tags for deals and top picks
- 🎯 Sticky navigation with smooth scrolling

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Load Sample Data

```bash
python manage.py load_sample_data
```

### 4. Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the site!

Visit `http://localhost:8000/admin` to access the admin panel.

## Project Structure

```
DOMPizza/
├── DOMPizza/              # Main Django project settings
├── pizza_menu/            # Pizza menu app
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin configuration
│   └── management/       # Custom management commands
├── templates/            # HTML templates
│   └── menu.html        # Main menu page
├── static/              # Static files
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   └── js/
│       └── main.js     # JavaScript functionality
└── manage.py           # Django management script
```

## Key Features Explained

### Cart Functionality
- Add items to cart with quantity management
- Cart persists using localStorage
- Modal popup for cart review
- Real-time cart count display

### Menu Management
- Organized by categories
- Support for tags (TOP PICK, DEAL)
- Price and calorie information
- Signature items marked

### Responsive Design
- Mobile-first approach
- Touch-friendly interface
- Adaptive grid layouts
- Optimized for all screen sizes

## Tech Stack

- **Backend**: Django 5.x
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Database**: SQLite (default, can be changed)
- **Fonts**: Inter (Google Fonts)

## Customization

### Adding New Menu Items
Use the Django admin panel at `/admin` to add, edit, or remove menu items, categories, and toppings.

### Modifying Colors
Edit the CSS variables in `static/css/style.css`:

```css
:root {
    --primary-red: #e31837;
    --dark-bg: #1a1a1a;
    /* ... more variables ... */
}
```

### Adding Images
Set the `image` URL field for menu items in the admin panel or through the API.

## Future Enhancements

- [ ] User authentication and profiles
- [ ] Order placement and checkout
- [ ] Payment integration
- [ ] Order tracking
- [ ] Custom pizza builder with visual interface
- [ ] Delivery address management
- [ ] Order history

## License

This project is for educational purposes.

## Credits

Design inspired by MOD Pizza's ordering interface.

# DOMPizza
