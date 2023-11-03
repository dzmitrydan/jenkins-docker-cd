>Please use branch ```flask-app-docker``` for this task that already exist in your forked repository after you has been started task
# flask-app-docker

Dockerize flask project from the previous tasks.

- [ ] Create Dockerfile. On the start flask application has to be launch
- [ ] Set application host to 0.0.0.0 (default is 127.0.0.1)
- [ ] Create build.sh to build image with _flask-app_ name
- [ ] Create _docker-compose_ file to start application.

Push into the repository:
- Dockerfile
- Modified start.py
- build.sh
- docker-compose.yml


### Install Jenkins (Windows 10)
```
docker run -d -p 8082:8080 --name "jenkins" -v jenkins_home:/var/jenkins_home -v //var/run/docker.sock:/var/run/docker.sock -v //var/opt/jenkins:/var/opt/jenkins liatrio/jenkins-alpine
```

- Username: `admin`
- Password: `admin`

Installed Jenkins plugins:
- Docker Pipeline
- Docker plugin
- Git plugin
- Groovy
- Pipeline

Branches:
- main
- dev

![Jenkins screenshot](readme-assets/jenkins-1.png)

### Jenkins settings
#### Regular Jenkins pipeline
![Jenkins settings screenshot](readme-assets/regular-pipeline-1.png)
![Jenkins settings screenshot](readme-assets/regular-pipeline-2.png)
![Jenkins settings screenshot](readme-assets/regular-pipeline-3.png)
![Jenkins settings screenshot](readme-assets/regular-pipeline-4.png)

#### Multibranch Jenkins pipeline
![Jenkins settings screenshot](readme-assets/multibranch-pipeline-1.png)
![Jenkins settings screenshot](readme-assets/multibranch-pipeline-2.png)
![Jenkins settings screenshot](readme-assets/multibranch-pipeline-3.png)
![Jenkins settings screenshot](readme-assets/multibranch-pipeline-4.png)
![Jenkins settings screenshot](readme-assets/multibranch-pipeline-5.png)

#### Docker
![Docker screenshot](readme-assets/docker-1.png)
