# Strega

Django App for retrieving Virginia ABC Store pricing data.

# Setup

## VirtualEnv
```
strega$ python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt
```

### Activate VirtualEnv
```
strega$ source venv/bin/activate
```

# Serve

With [VirtualEnv activated](#activate-virtualenv), run:
```
(venv) strega/strega$ python3 manage.py runserver 8080
```

# Migrate
With [VirtualEnv activated](#activate-virtualenv), run:
```
(venv) strega/strega$ python3 manage.py migrate
```

# Make Migrations
```
(venv) strega/strega$ python3 manage.py makemigrations bevendo
```
