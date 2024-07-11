from datetime import timedelta

from celery import Celery

cel = Celery("celery_demo",
             broker='redis://192.168.52.128:6379/2',
             backend='redis://192.168.52.128:6379/1',
             include=['celery_tasks.task01', 'celery_tasks.task02'])

cel.conf.timezone = 'Asia/Shanghai'

cel.conf.enable_utc = False

# celery -A celery_tasks worker -l info -P eventlet
# celery -A celery_tasks beat -l info -P eventlet
# 注意需要先处理遗留任务
cel.conf.beat_schedule = {
    "add-every-10-seconds": {
        'task': 'celery_tasks.task01.send_email',
        'schedule': timedelta(seconds=6),
        'args': ('张三',)
    }
}
