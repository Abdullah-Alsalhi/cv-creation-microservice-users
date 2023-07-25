#!/bin/bash

if ! command -v helm &> /dev/null
then
    echo "helm tool not found, please install it first and try again."
    exit
fi

dbname=`cat ./app_config.yaml | grep -i "DB_NAME:" | awk {'print $2'}`
dbuser=`cat ./app_config.yaml | grep -i "DB_USER:" | awk {'print $2'}`
dbpass=`cat ./app_secret.yaml | grep -i "DB_PASSWORD:" | awk {'print $2'} | base64 -d`

helm repo add bitnami https://charts.bitnami.com/bitnami

echo "Executing..."

echo "helm install my-postgresql bitnami/postgresql --version 11.9.13 --set global.postgresql.auth.username=$dbuser --set global.postgresql.auth.password=$dbpass --set global.postgresql.auth.database=$dbname "
helm install my-postgresql bitnami/postgresql --version 11.9.13 --set global.postgresql.auth.username="$dbuser" --set global.postgresql.auth.password="$dbpass" --set global.postgresql.auth.database="$dbname"


