import os
 from celery import Celery
 from django.conf inport settings

 # load the settings for celery
 os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

 app = Celery('myshop')

 app.config_from_object('django.conf:settings')
 app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
