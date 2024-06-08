# myapp/tasks.py

from celery import shared_task


@shared_task
def my_celery_task():
    print("start")
    import time

    time.sleep(10)
    print("end")
