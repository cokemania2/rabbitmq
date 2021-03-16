celery -A  tasks2 worker --loglevel=DEBUG -c 6
or 
celery -A tasks2 worker -Q moon_queue --loglevel=DEBUG

실행 : python3 run_tasks.py