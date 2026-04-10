from celery import Celery
import time

app = Celery(
        "demo",
        broker="redis://localhost:6379/0",
        backend="redis://localhost:6379/0"
)

# @app.task 를 통해 decorate하는 함수는 celery에게 맡길 함수
@app.task
def slow_add(a, b):
    time.sleep(5)
    return a+b

