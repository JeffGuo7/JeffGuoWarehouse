from celery.result import AsyncResult
from celerydemo.celerydemo1.celery_task import cel

async_result = AsyncResult(id="cf16b0f8-cb6d-49d1-88c8-d3f5949c7e9a",app=cel)

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