#pasos para configurar postgres en un sistema Debian 
#modificar los nombres de usuario, base de datos y contraseña
usuario=***
pass=***
app=***
apt install postgresql python3-psycopg2
su postgres
psql -c "create user '$usuario' with password '$pass' LOGIN;"
psql -c "alter user '$usuario' set default_encoding to 'utf8';"
psql -c "alter user '$usuario' set timezone to 'UTC';"
psql -c "create database '$app';"
psql -c "grant all on database '$app' to '$usuario';"
exit

