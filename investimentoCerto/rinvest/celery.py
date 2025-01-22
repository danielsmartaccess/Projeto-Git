import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rinvest.settings')

app = Celery('rinvest')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Configure periodic tasks
app.conf.beat_schedule = {
    'update-financial-indicators': {
        'task': 'apprinvest.tasks.update_financial_indicators',
        'schedule': crontab(minute='*/5'),  # Executa a cada 5 minutos
    },
    'fetch-financial-news': {
        'task': 'apprinvest.tasks.fetch_financial_news',
        'schedule': crontab(minute='*/15'),  # Executa a cada 15 minutos
    },
}
