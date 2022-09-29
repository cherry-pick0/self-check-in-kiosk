# To make sure that your Celery app is loaded when you start.sh.sh.sh Django,
# you should add it to __all__:
from .celery import celery_app

__all__ = ("celery_app",)
