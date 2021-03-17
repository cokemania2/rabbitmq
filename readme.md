install
```
sudo apt-get install -y rabbitmq-server
sudo pip install celery
sudo service rabbitmq-server status
```
Add a new/fresh user, say user test and password test
```
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
```

```
celery -A  tasks2 worker --loglevel=DEBUG -c 6
```
or 
```
celery -A tasks2 worker -Q moon_queue --loglevel=DEBUG
```

실행 : 
```
python3 run_tasks.py
```