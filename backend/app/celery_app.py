from celery import Celery
import os

# Ensure required environment variables are set
REDIS_URL = os.getenv('REDIS_URL')
if not REDIS_URL:
    raise EnvironmentError('REDIS_URL environment variable is required')

celery_app = Celery(
    'devpulse',
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
