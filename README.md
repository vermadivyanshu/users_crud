## Team Members CRUD

### Installation
#### Install pipenv
Installing pipenv using pip
```
pip install pipenv
```
From the root directory, run the following:
```
pipenv shell #create and activate environment
pipenv install #install packages
```
To run the server, run the following from the root directory:
```
python manage.py migrate
python manage.py createsuperuser #to create super user for logging in to view the routes
python manage.py runserver #runs local server
Server runs on http://127.0.0.1:8000/
```

### Running tests
```
python manage.py test
```

### Running development server
```
python manage.py migrate
python manage.py runserver
```

### Scope
The following can be improved in the project:
1. Adding infinite scroll in the user list page
2. Slight tweaks in responsiveness by adding media queries
3. adding flash messages for success
4. adding error message for 404 or flash messages
