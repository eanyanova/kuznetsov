**Deployment steps:**
- pip install -U -r requirements.txt
- python manage.py migrate --no-input
- python manage.py bower install
- python manage.py collectstatic --no-input