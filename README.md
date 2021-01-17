# DUID
[![codecov](https://codecov.io/gh/azharaiz/duid/branch/master/graph/badge.svg)](https://codecov.io/gh/azharaiz/duid)

Open source expense tracker.

## Technologies
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt)
- [Docker](https://www.docker.com/)

## Setup Development
Make sure docker installed on your machine. Follow [this steps](https://docs.docker.com/install/) 
for docker installation.

```
# Migrate
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

# Start the application
docker-compose up
   
# Stop the aplication
docker-compose down

# Test
docker-compose run web python manage.py test
```

## Tasks
### Sprint 1
- Init TECH [AZHAR]
- Dockerize Project [AZHAR]
- Authentication [AZHAR]
- CRUD dompet [KEVIN]
- CRUD category [FERIL]
- Continuous Integration [FERIL & KEVIN]
- Codecov [KEVIN]

### Sprint 2
- CRUD transaction [FERIL]
- Read transaction with Filter [FERIL]
- Target [KEVIN]
- Register User [AZHAR]
- Integration Test [AZHAR]

### Sprint 3
- Add pylint [FERIL]
- Refactor Code Smell [ALL]
- Update database to PostgreSQL[AZHAR]

## Teams
- 1706075041 - Kevin Raikhan Zain
- 1706074865 - Muhammad Azhar Rais Zulkarnain
- 1706075054 - Muhammad Feril Bagus Perkasa
