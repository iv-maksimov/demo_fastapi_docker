# Демо проект по fastapi и docker

### Start app for dev

`uvicorn app.main:app --reload`

### Docker
#### Build docker image

`docker build -t demo_app .`

#### Run app

`docker run -d --name demo_app_cont -p 8001:8001 demo_app`