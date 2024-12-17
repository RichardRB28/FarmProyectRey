crear archivos de requerimientos se usa pip freeze > requirements.txt

(Settings)

- definir zonas horarias
- definir directorio raiz
- definir los templates con el dir raiz
'DIRS': [BASE_DIR / 'templates'],
- Definir la base de datos a usar con usuario, contraseña y nombre

* Despues de descargar sql server dirigirse a cd /ect/postgresql/16/main/
 editar los archivos pg_hba e ident donde en hab se añade la linea 

host	all	127.0.0.1/32	md5 

para autorizar el ingreso por contraseña


despues de crear una app con el comando

python manage.py startapp ___ nombre

debe registrarse en el settings en la parte APP INSTALED

Para ejecutar comandos psql deesde la consola se usa

psql -p (puerto) -h (ipdir) -U (usuario postgres) -c "sentencia sql;"
