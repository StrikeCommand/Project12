# Project12

### Requirements

Angular>=14

Docker

### Build 
```
docker compose build
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
```
Next run command

`docker compose run web python manage.py createsuperuser`

Enter your desired username and press enter.

`Username: admin`

You will then be prompted for your desired email address (it is optional):

`Email address: admin@example.com`

The final step is to enter your password. 
You will be asked to enter your password twice, 
the second time as a confirmation of the first.

```
Password: **********
Password (again): *********
```

### Start project

```
docker compose up
ng serve
```

### Endpoints
- admin panel link: http://127.0.0.1:8000/admin/
- get all cities: http://127.0.0.1:8000/api/cities/
- get city points: http://127.0.0.1:8000/api/cities/<int:id>/
- get point details: http://127.0.0.1:8000/api/points/<int:id>/