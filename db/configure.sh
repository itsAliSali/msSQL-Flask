#!/bin/bash

STRONG_PASSWORD="Qwer22@@"

sudo docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=$STRONG_PASSWORD"\
                --name sql_server -p 1433:1433 -d \
                mcr.microsoft.com/mssql/server:2022-latest

sudo docker exec -u 0 sql_server mkdir /data
sudo docker cp ./prj1.sql sql_server:/data
sudo docker cp ./alter.sql sql_server:/data
sudo docker cp ./data.sql sql_server:/data

sudo docker exec sql_server /opt/mssql-tools/bin/sqlcmd -U sa -P $STRONG_PASSWORD -i /data/prj1.sql
sudo docker exec sql_server /opt/mssql-tools/bin/sqlcmd -U sa -P $STRONG_PASSWORD -i /data/alter.sql
sudo docker exec sql_server /opt/mssql-tools/bin/sqlcmd -U sa -P $STRONG_PASSWORD -i /data/data.sql


