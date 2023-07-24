# djangoProject/celery.py

from celery import Celery

# Create the Celery instance for the djangoProject project
celery_app = Celery('djangoProject', broker='redis://localhost:6380/0')
