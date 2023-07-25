# User System Registration

## Project Idea:

Microservce system to register/login users.

## List of Services / Features:

- Register user and assign JWT to him.
- Login user and assign JWT to him.

## To run this locally :

- clone this repo

```
git clone https://github.com/Abdullah-Alsalhi/cv-creation-microservice-users.git
```

- Insure to cd to the project directory

```
cd cv-creation-microservice-users
```

- Insure you have python >= 3.11.x
- Inusure you have pip installed
- Insure you are in virtual environment by running:

```
python3 -m venv venv
```

- Insure to activate the virtual environment by running :

```
source venv/bin/activate
```

- Insure to install the requirments.txt

```
pip install -r requiremnets.txt
```

- Create .env file

``` shell
cp .env.example .env
```
Make sure to write the database connection properties <b>DB_NAME</b> ,  <b>DB_USER</b> , <b>DB_PASSWORD</b>.

You can change the database type by change the <b>ENGINE</b> value in .env file, by default is Postgres database.

- Execute migreate command 
``` shell
python manage.py migrate
```

- Insure to run the app before request to it

```
python3 manage.py runserver
```

## Run applicaiton using Docker 🐬 :
You have to install [docker-compose](https://docs.docker.com/compose/install/) in your machine fist.<br>
Make sure the ports <b>8000</b> and <b>5432</b> are available.

- Run the docker compose command:

``` shell
docker-compose up -d
```

- Check the continer status:

``` shell
docker-compose ps
```

## Run applicaiton using kubernetes ☸ :
First of all make sure you has [Helm](https://helm.sh/docs/intro/install/) installed on your machine, becaues we will used to install the Postgres database deployment.

Enter kubernetes directory in this project
``` shell
cd k8s/
```

Applying helm to run Postgres database.
``` shell
chmod u+x deploy_psql.sh
./deploy_psql.sh
```

Apply the mainfests files of application.
```shell
kubectl apply -f .
```

Verified the status of pods
```shell
kubectl get pods
```
if everything is running, you can access the application throw,<br>
http://localhost:31480


# Routes:

- Post request to => http://localhost:8000/user/register/

```
REQUEST BODY => {
    "email": "YOUR_EMAIL",
    "password": "YOUR_PASSWORD"
}

```

- On Faliure :

```
RESPONSE BODY => {
    "email": "Error message",
    "password": "Error messge"
}
```

- On Success :

```
RESPONSE BODY => {
    "data": "User Data",
    "access_token": "JWT_TOKEN"
}
```

- Post request to => http://localhost:8000/user/login/

```
REQUEST BODY => {
    "email": "YOUR_EMAIL",
    "password": "YOUR_PASSWORD"
}

```

- On Faliure :

```
RESPONSE BODY => {
    "email": "Error message",
    "password": "Error messge"
}
```

- On Success :

```
RESPONSE BODY => {
    "data": "User Data",
    "access_token": "JWT_TOKEN"
}
```
