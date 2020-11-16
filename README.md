# Cartas-OficiosAPP
Este repositorio contiene un proyecto de seguimiento de cartas u oficiones del observatorio del desarrollo de la UCR.

Este proyecto sigue el patrón Modelo-Vista-Template.

(ver aquí : https://docs.hektorprofe.net/django/web-personal/patron-mvt-modelo-vista-template/)


## Pasos de instalación (para desarrollar en caso de ser necesario)

1. Crear un entorno virtual para trabajar. Debe ir a la carpeta raíz donde está el proyecto, abrir una consola y correr lo siguiente : 
```
python3 -m pip install --upgrade pip
```
```
pip3 install virtualenv
```

2. Una vez creado el entorno virtual debe activarlo (en windows) :
```
.\entorno\Scripts\activate
```

En linux se activa así :
```
source entorno/bin/activate
```
Cuando vea que su consola tiene el nombre del entorno virtual, está activado, para desactivarlo solo escriba la palabra deactivate en la consola. Recuerde siempre correr el entorno virtual para probar el app.

3. Con el entorno virtual activado, vaya a la carpeta donde se encuentra el archivo requirements.txt y con la terminal abierta corra lo siguiente :
```
pip install -r requirements.txt
```

Esto hará que usted tenga todas las dependencias necesarias para correr el proyecto.

4. Vaya al archivo database_conf.py.sample en appOficios\appOficios y siga las indicaciones.

5. Corra las migraciones para crear en la base de datps las tablas de autenticación de usuarios y las tablas especificadas en los modelos del proyecto. Para esto vaya a la carpeta donde se encuentra el archivo manage.py del proyecto y corra el siguiente comando : 
```
python manage.py migrate
```
Es importante mencionar que en este caso se trabajará con postgresql en el ambiente de desarrollo y lo más recomendable es que sea el mismo en producción.

6. Cree un usuario para poder entrar al panel de administración, para esto corra el siguiente comando en la misma ubicación anterior:
```
python manage.py createsuperuser
```

Para acceder a la administración debe ingresar al siguiente enlace : http://localhost:8000/admin (esto en desarrollo, en producción debe usar su propio host y puertos en lugar de localhost:8000, por ejemplo -> https://myhost:1234/admin)

7. Una vez realizados estos pasos puede correr el app con el siguiente comando e ingresar a http://localhost:8000 (o la dirección asignada para producción):
```
python manage.py runserver
```

## Llevando a producción

Para llevar a producción el app siga las intrucciones en los siguientes en enlaces: 

Para hacer deploy con https: https://certbot.eff.org/instructions

Para hacer deploy del app en servidor con Linux : http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/

Siempre es importante leer la documentación oficial : https://docs.djangoproject.com/en/3.1/howto/deployment/


Nota: esta aplicación posee la funcionalidad para eliminar oficios, para activarla solo debe ir al archivo oficio_list.html y oficio_update_form.html en la ruta \appOficios\oficios\templates\oficios\ y eliminar los bloques {% comment %} y {% endcomment %}.Además debe ir al archivo home.html y eliminar la línea 48 para quitar la frase de temporalmente no disponible.

##### version 3.0
