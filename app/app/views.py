# views.py (inside your Django app)
from django.shortcuts import render
from .tasks  import app

def index(request):
    # Your view logic
    print("tesst")
    data = "test"
    result = app.send_task('run_ml_task', args=[data], queue='ml_queue')
    print(result.get())
    print("Test")

    return render(request, 'index.html', {'result_data': result.get()})
