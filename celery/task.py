from celery_app import slow_add

result = slow_add.delay(3, 7)
print(result.id)

