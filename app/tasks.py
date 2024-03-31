from celery import Celery, shared_task
#from celery.decorators import task
from django.core.cache import cache
from .utils import get_data

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

@shared_task(name="fetch_data_from_url")
def fetch_data_from_url():

    data = get_data()
    message = data[0]["text"]
    logger.info("activated fetch data function")
    print(message)
    cache.set('message', message)
