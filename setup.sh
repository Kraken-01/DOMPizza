#!/bin/bash

echo "🍕 Setting up DOM Pizza Ordering Site..."
echo ""

# Create migrations
echo "Creating database migrations..."
python manage.py makemigrations
python manage.py migrate

# Load sample data
echo ""
echo "Loading sample menu data..."
python manage.py load_sample_data

# Create superuser (optional)
echo ""
echo "Would you like to create an admin user? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    python manage.py createsuperuser
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the development server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://localhost:8000"
echo "Admin panel: http://localhost:8000/admin"

