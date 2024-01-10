
![Venzo Logo](https://venzotechnologies.com/static/media/logo.20c3af3bf8b6aedba1ed0e68ca927882.svg)

# Venzo Django Starter Pack

Welcome to the venzo Django Starter Pack! This starter pack is designed to help you kickstart your Django projects with some essential configurations and features.

## Getting Started

Follow these steps to get your project up and running:

### Prerequisites

Make sure you have the following installed on your machine:


#### install docker 

https://docs.docker.com/engine/install/



#### required packages
- [Python](https://www.python.org/downloads/) (3.11 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [flake8](https://pypi.org/project/flake8/)
- [pylint](https://pypi.org/project/pylint/)

For installation copy the below section 

```bash
    pip install flake8 pylint
```

#### required vs code extensions

1. [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2. [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
3. [black formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
4. [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
5. [Github actions](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions)
6. [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
7. [Django2](https://marketplace.visualstudio.com/items?itemName=bigonesystems.django)
8. [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)


### Clone the Repository
```bash
git clone -b postgres https://github.com/venzo-tech/venzo_django_starter.git
cd venzo_django_starter
```

### run via docker 

#### do the collecstatic and migrations
```bash
docker-compose run django python manage.py collectstatic
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```


#### create superuser if required

```bash
docker-compose run django python manage.py createsuperuser
```

#### build and run
```bash
docker-compose build
docker-compose up
```


### run pre-commit and push to your repo 

```bash
pre-commit run --all-files
```