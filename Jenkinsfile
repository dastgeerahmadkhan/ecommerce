pipeline {

agent any

stages {

stage('Clone Repo') {

steps {

git 'https://github.com/username/django-ecommerce.git'

}

}

stage('Build Docker Image') {

steps {

sh 'docker build -t django-ecommerce .'

}

}

stage('Stop Old Container') {

steps {

sh 'docker rm -f django_container || true'

}

}

stage('Run Container') {

steps {

sh 'docker run -d -p 8000:8000 --name django_container django-ecommerce'

}

}

}

}