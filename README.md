# metrobuses_cdmx
Pipeline de análisis de datos utilizando los datos abiertos de la Ciudad de México correspondientes a las ubicaciones de las unidades del metrobús para que pueda ser consultado mediante un API Rest filtrando por unidad o por alcaldía.

# Reproducción del repositorio

Dependencias de reproducción:
* Docker 🐳
* Docker-compose

Ejecuta el siguiente comando en la raíz del proyecto:
```
docker-compose -f docker-compose.yml up -d
```
Para validar que el repositorio se levantó correctamente, ejecuta el siguiente curl en la terminal:
```
curl -X 'GET' \
'http://0.0.0.0:8080/status' \
-H 'accept: application/json'
```
Para probar el funcionamiento de los endpoints se puede acceder a la documentación de swagger:
[SWAGGER DOC](http://0.0.0.0:8080/docs#/)
