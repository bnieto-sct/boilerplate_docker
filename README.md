# Django Docker Full - by Peacedev Team

![](https://peacedev.co/image/logopeacedevletra.png)
![](https://i.imgur.com/rsEw4yc.png)

El código del backend de encuentra dentro de la carpeta **app**

Requisitos tecnicos para poder correr el backend
- Tener docker instalado en la maquina donde se va a ejecutar el proyecto
- Configurar las variables de entorno
- Ejecutar los comandos de migracion y creacion de super usuario en orden

### Configurar el entorno por primera vez
en la raiz del proyecto existe un archivo llamado** env.template**
este archivo contiene nuestras variables de entorno con valores por defectos
usted puede cambiarlos por los valores que quiera

**nota: no recomiendo cambiar el host de postgres si vamos a ejecutar nuestro ambiente de manera local**

Para que el backend pueda funcionar debe usted hacer una copia del archivo con el siguiente comando:

`cp env.template .env`

Una vez copiado se puede iniciar con la construccion de la imagen de docker y posteriormente la puesta en marcha de esta misma, para hacerlo puede utilizar el siguiente comando:

`docker-compose up -d --build`


Si todo sale done podremos ir al [http://0.0.0.0:4500/](http://0.0.0.0:4500/ "http://0.0.0.0:3002/") donde vive nuestra app y podremos ver la documentación de la api.

Lo siguiente que debemos hacer es seguir estos comandos para aplicar las migraciones y crear un usuario en nuestro administrador:
- `docker-compose exec app python3 manage.py makemigrations`
- `docker-compose exec app python3 manage.py migrate`
Nota: También podemos ejecutar el script `./run_migrate.sh`

Para crear un super usuario en nuestro administrador debemos ejecutar el siguiente comando:

`docker-compose exec app python3 manage.py createsuperuser`
Nota: También podemos ejecutar el script `./run_create_user.sh`

Para poder hacer uso de nuestro backend debemos crear las tiendas en el admin y usuarios de las tiendas, luego debemos logearnos en nuestra aplicación de angular y podemos ver funcionando la aplicación conectada al backend.

Si queremos detener nuestra imagen podemos hacerlo con este comando:

`docker-compose stop`

Si queremos volver a levantar nuestra nuevamente:
`docker-compose up -d`

Nota: También podemos ejecutar el script `./run_rebuild.sh` para hacer ambas cosas en un sólo comando

Si quieres desplegar este proyecto en producción, [copia este código](https://gist.github.com/peacedevteam/ff4043930520088d55710afd8ef8eda8)  

Gracias por usar nuestro proyecto. **Si tienes alguna duda sientete libre de contactarnos hello@peacedev.co**.
Agradecimientos especiales para todo nuestro equipo por el soporte.

### Hecho con 💜 por [Peacedev Team](http://peacedev.co)

## Disfruten del proyecto 💜 💚 💛 🥳
