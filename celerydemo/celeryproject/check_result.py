from celery.result import AsyncResult
from celery_tasks.celery import cel

async_result = AsyncResult(id="1c43e25b-6833-4c43-b25e-35286943fd3e",app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
    # result.forget() 将结果删除
elif async_result.failed():
    print("执行失败")
elif async_result.status == 'PENDING':
    print("任务等待中")
elif async_result.status == 'RETRY':
    print("任务异常后正在重试")
elif async_result.status == 'STARTED':
    print('任务已经开始被执行')