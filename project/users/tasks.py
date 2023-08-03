from celery import shared_task
import time


@shared_task
def divide(x, y):
    # to debug celery
    # from celery.contrib import rdb
    # rdb.set_trace()

    time.sleep(5)
    return x / y
