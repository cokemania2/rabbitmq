celery -A  tasks2 worker --loglevel=info -c 6
or 
celery -A tasks2 worker -Q moon_queue --loglevel=info

실행 : python3 run_tasks.py