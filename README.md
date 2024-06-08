## Setup
```bash
virtualenv -p python3.11 env
```
```bash
source env/bin/activate
```

### Build full project
```bash
docker-compose up --build
```
### Build specific container
```bash
docker-compose build web
```


### Connect to pg container (FOR WHAT????)
```bash
docker-compose exec db psql -U postgres
```

### Connect to django_shell
```bash
docker-compose run web python manage.py shell_plus
```


### Create super-duper-user
```bash
docker-compose exec web python manage.py createsuperuser
```
