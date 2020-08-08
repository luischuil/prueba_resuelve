# Prueba Ingeniería Resuelve
Api para resolver la prueba de ingeniería resuelve.

## Requerimientos
Para probar la api se requiere tener instalado docker y docker compose.

## Instalación
```python
#Clonar el repositorio.
$ git clone git@github.com:luischuil/prueba_resuelve.git

#En la carpeta raiz del proyecto ejecutar el siguiente comando para iniciar la api.
$ docker-compose up
```
>Nota: si el comando falla intente con: $ sudo docker-compose up

## Solución
Se creó un endpoint que calculará el sueldo completo de cada jugador del equipo resuelve:
```
POST http://localhost:8000/payroll_resuelve
```
El endopint recibe en el `body` un json con el siguiente formato: [Ver ejemplo](https://github.com/luischuil/prueba_resuelve/blob/master/resuelve/app/fixtures/request_payroll_resuelve.json) 

## Bonus
Para el bonus se creó un segundo endpoint:
```
POST http://localhost:8000/payroll_teams
```
Éste endpoint recibe en el `body` un parámetro adicional `teams` donde se especifica los objetivos a alcanzar por cada equipo. El formato esperado es el siguiente: [Ver ejemplo](https://github.com/luischuil/prueba_resuelve/blob/master/resuelve/app/fixtures/request_payroll_teams.json)

## Unit test
Si desea ejecutar las pruebas unitarias en la raíz del proyecto ejecute el siguiente comando:
```
$ docker exec -it <container-id> python /code/resuelve/manage.py test app
```
Para obtener el `container-id`, asegurese de que la api esté corriendo y ejecute el comando:
```
$ docker ps
```
Obtendrá un resultado como el que sigue:
```
CONTAINER ID     IMAGE                       COMMAND
ada2267d34a3     prueba_resuelve_web_django  "python /code/resuel…"
```
Sustituya el `container-id` en la primera sentencia y ejecute el comando.