# 굳이 따지자면.. Flask 부분에 해당 (task를 던지니까)

from celery_app import slow_add

result = slow_add.delay(3, 7) # task를 Celery의 broker(우리의 경우 Redis)에 넣음
print(result.id)
