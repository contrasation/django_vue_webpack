import time
# http://agiliq.com/blog/2015/07/getting-started-with-celery-and-redis/
from celery import Celery
from celeryconfig import CELERY_RESULT_BACKEND
app = Celery('celery', broker='redis://localhost:6379/0', backend=CELERY_RESULT_BACKEND)


@app.task
def run():
    time.sleep(10)
    print 'Process was done.'
    return 'Done!'


@app.task
def calc(a, b):
    return a + b
