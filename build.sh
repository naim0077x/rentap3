#!/bin/bash
echo "🚀✨ Deploying Rentahouses web app 🌍🏡 (all rights reserved by Rentahouses 2025) 🎉🔥"
echo "🔧🛠️ Starting build process... 🚀💨"
set -e
echo "📦🔍 Installing Python dependencies... 🐍📂"
pip install -r requirements.txt
echo "🔄📜 Applying migrations... 🚀🔧"
python manage.py migrate
echo "📂📥 Collecting static files... 🎨🖼️🗂️"
python manage.py collectstatic --noinput
echo "✅🎉 Build process completed successfully! 🎯🎊🎆"
echo "🚀🔥 Starting server... 💻🌍🛠️💨"

# gunicorn rentahouses.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 4 --timeout 300
