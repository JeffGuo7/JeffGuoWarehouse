import celery
import time

backend = 'redis://192.168.52.128:6379/1'
broker = 'redis://192.168.52.128:6379/2'
cel = celery.Celery('test', backend=backend, broker=broker)


@cel.task
def send_email(name):
    print("向%s发送邮件..." % name)
    time.sleep(5)
    print("向%s发送邮件完成" % name)
    return "ok"


# celery -A celery_task worker -l info -P eventlet