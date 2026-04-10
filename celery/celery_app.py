from celery import Celery
import time

app = Celery(
        "demo",
        broker="redis://localhost:6379/0", # 작업 큐
        backend="redis://localhost:6379/0" # 저장소
)

# @app.task 를 통해 decorate하는 함수
# celery 명령어를 통해 생성된 백그라운드 worker 프로세스가 이러한 함수를 처리
@app.task
def slow_add(a, b):
    time.sleep(5)
    return a+b

