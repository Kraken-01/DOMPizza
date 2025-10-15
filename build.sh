#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Load sample data (optional - comment out if you don't want sample data on every deploy)
python manage.py load_sample_data || true

