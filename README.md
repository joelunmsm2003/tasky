Tasky
=====

Tasky es un sistema de tareas para administrar las incidencias y requerimientos de clientes 


Quick Start
===========

cd /ticket/mysite/redis-3.0.2
src/redis-server

cd /ticket/mysite
python manage.py runserver 0.0.0.0:8000&

Requerimientos
==============

Django
pip install Django==1.7.4
pip install django-redis-sessions
pip install django-websocket-redis
pip install simplejson


Redis
wget http://download.redis.io/releases/redis-3.0.2.tar.gz
tar xzf redis-3.0.2.tar.gz
cd redis-3.0.2
make

Mysql
sudo apt-get install build-essential python-dev libmysqlclient-dev
apt-get install python-MySQLdb
sudo apt-get build-dep python-mysqldb
pip install MySQL-python

Data Inicial
python manage.py migrate
python manage.py loaddata ini.json


Comandos Git
============

git add .
git commit -m 'info'
git push [origen] [rama]
#Listar ramas git branch 
#Crear rama git branch [rama]
#Ingresar rama git checkout [rama] 

##Eliminar
git remote rm [rama]
git branch -d [rama]



Web2py
======

#Iniciar web2py  
python web2py.py  runserver

#Iniciar tarea scheduler
python web2py.py -K name_app -D 0

#Iniciar shell
python web2py.py -S name_app -M

#tablas en base de datos
db.tables
db.table_name.fields

#Consulta a base de datos
db(db.tables_name.id==1).select()
db(db.tables_name.id>0).count()



//Instalacion
pip install Django==1.7
apt-get install python-MySQLdb
pip install django --upgrade
pip install simplejson



python manage.py syncdb 
python manage.py inspectdb > MonitorApp/models.py


--Agregar un grupo a un usuario
grupo=get_object_or_404(Group,name='Clientes')
c.groups.add(grupo)

--Select del grupo de un usuario
x=User.objects.get(pk=2)
x.groups.all()

--Listar
User.objects.all().values_list('id')

 User.objects.filter(groups__name='Soporte')


--Listar

x=Ticket.objects.get(id=1)
x.soporte_set.all()

python manage.py makemigrations MonitorApp


--Agregar un campo

python manage.py makemigrations
python manage.py syncdb

python -c "import django; print(django.get_version())"

eliminar django
ruta 
python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"

from django.db.models import Max

x.soporte_set.all().aggregate(Max('id'))

group by

Soporte.objects.values('ticket_id').annotate(dcount=Count('ticket_id'))

Soporte.objects.values('ticket_id').annotate(dcount=Max('fecha_inicio'))


django-admin.py startproject mysite


SQL Designer
andyjo-1

…or create a new repository on the command line

sudo apt-get install python-mysqldb

lsof -i:22


touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:joelunmsm2003/ticket.git
git push -u origin master
…or push an existing repository from the command line


git remote add origin git@github.com:joelunmsm2003/ticket.git
git push -u origin master



192.168.1.248
 x13nc14s


git init
git add *
git commit -m "Initial import"
git remote add xdev git+ssh://192.168.1.248/home/repository.git
git push xdev master


df -h

Ir a un commit anterior y crear una rama
git checkout -b <commit>

Cambiar de nombre de la rama

git branch <commit actual> <commit nuevo>
ver las ramas

Hacer un commit en la rama

git commit -m -a 'name'

Traer los cambios del pasado

git checkout master
git merge <rama>

git clone git+ssh://root@192.241.177.135/home/ticket.git
git clone ssh://root@192.241.177.135/home/repositorio.git

git@192.168.1.247:/home/git/repositories/admin/tickets.git

ftibywfbkupr


Esto pertenece a la a newrama

git commit -a -m '1commit'

Esto es del branch1

estoy en la rama prueba

Base de Datos
=============

- Enterprise
IP Address: 198.199.76.147
Username: root
Password: hbnzeniovgnm

- Extras
IP Address: 162.243.57.9
Username: root
Password: xfwlmkvdlhgi

- Apps
IP Address: 192.241.177.135
Username: root
Password: ftibywfbkupr


LLaves en Linux
===============

ssh-keygen
cd .ssh
ls .ssh/
cat id_rsa.pub >> .ssh/authorized_keys 
scp .ssh/id_rsa.pub root@192.241.177.135:/root/
mcedit .ssh/authorized_keys 








