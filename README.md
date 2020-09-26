# Cartas-OficiosAPP
Este repositorio contiene un proyecto de seguimiento de cartas u oficiones del observatorio del desarrollo de la UCR.

Este proyecto sigue el patrón Modelo-Vista-Template.

(ver aquí : https://docs.hektorprofe.net/django/web-personal/patron-mvt-modelo-vista-template/)

Al descargar este repositorio debe seguir los pasos de la siguiente sección después de haber leído el documento en el siguiente enlance : https://docs.google.com/document/d/1_RzAEx51PmbtBb9QpGnxVg5YEjERllOf94-e4su-jy0/edit?usp=sharing


## Pasos de instalación

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
Cuando vea que su consola tiene el nombre del entorno virtual, está activado, para desactivarlo solo escriba la palabra deactivate en la consola. Recuerde siempre correr el entorno virtual para probar el app.

3. Con el entorno virtual activado, vaya a la carpeta donde se encuentra el archivo requirements.txt y con la terminal abierta corra lo siguiente :
```
pip install -r requirements.txt
```

Esto hará que usted tenga todas las dependencias necesarias para correr el proyecto.


4. Correr las migraciones para crear las tablas de autenticación de usuarios en la base de datos especificadas en los modelos. Para esto vaya a la carpeta donde se encuentra el archivo manage.py del proyecto y corra el siguiente comando : 
```
python manage.py migrate
```
Es impottante mencionar que en este caso se trabajará con sqlite en el ambiente de desarrollo.


5. Cree un usuario para poder entrar al panel de administración, para esto corra el siguiente comando en la misma ubicación anterior:
```
python manage.py createsuperuser
```

6. Una vez realizados estos pasos puede correr el app con el siguiente comando e ingresar a http://localhost:8000:
```
python manage.py runserver
```

##### version 1.0 (recuerde que esto es para ambiente de desarrollo)
