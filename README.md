# DevOps Microservices

## Preparation
1. Start a VM based on the "DevOps - Microservices" template
2. Open ports 1080 and 8500 on the firewall
3. Clone the https://github.com/szatmari/devops-microservices.git repository

## Python webservices
1. Test the python Pi application
```bash
cd pi
python3 pi.py
```
From an other terminal try the endpoint using curl

2. Test the python REST API
```bash
cd resource
python3 res.py
```
Test the GET, POST requests

## Microservices
We start each service one by one. You can try the HTTP interface using curl or in the browser through the reverse proxy 

1. Start the Pi and the rewerse proxy container and test the requests, check the logs
```bash
docker-compose up -d pi
docker-compose up -d nginx
curl localhost:1080/pi/20
docker-compose logs -f pi
```
2. Start the go container
```bash
docker-compose up -d go
curl localhost:1080/hello
```
3. Start the node container
```bash
docker-compose up -d node
curl localhost:1080/10pi
curl localhost:1080/techlist
```
4. Start the SpringBoot stack
```bash
docker-compose up -d mysql
docker-compose up -d webapp
curl localhost:1080/greeting
curl localhost:1080/sql
```
5. Start the Python REST API servcie
```bash
docker-compose up -d resource
curl localhost:1080/staff/Tamas
```
Check the API endpoints using Postman

6. Start the Consul servcie
```bash
docker-compose up -d consul
```
Visit the Consul UI in the browser (mapped port 8500)

7. Scale up the pi service
```bash
docker-compose up --scale pi=5 -d
```
Check the changes on the Consul Web UI

Test the requests
```bash
docker-compose logs -f pi
curl localhost:1080/hello
```
8. Start the HAProxy container
```bash
docker-compose up -d haproxy
```
Check the /haproxy endpoint in the browser
Test scaling up and down with the Pi service

9. Start the Jupyter service and check the /hub endpoint in the browser
```bash
docker-compose up -d jupyter
```
10. Integrate Jenkins to your reverse proxy

