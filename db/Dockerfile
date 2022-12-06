FROM mcr.microsoft.com/mssql/server:2022-latest

COPY ./prj1.sql /data/
COPY ./alter.sql /data/
COPY ./data.sql /data/

RUN /opt/mssql-tools/bin/sqlcmd -U sa -P $MSSQL_SA_PASSWORD -i /data/prj1.sql
# RUN /opt/mssql-tools/bin/sqlcmd -U sa -P Asdf22@@ -i ./data/alter.sql
# RUN /opt/mssql-tools/bin/sqlcmd -U sa -P Asdf22@@ -i ./data/data.sql

