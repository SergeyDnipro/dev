from django_prj.celery import app

@app.task
def foo_1(x, y):
    return x * y

@app.task
def foo_2(x, y):
    return x + y

# Запуск task(foo_3) 1 раз в минуту
@app.task
def foo_3(x, y):
    print(x - y)
