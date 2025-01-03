## 5.6 Environment management: Docker

<a href="https://www.youtube.com/watch?v=wAtyYZ6zvAs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-06.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)

## Installing Docker

To isolate more our project file from our system machine, there is an option named Docker. With Docker you are able to pack all your project in the system that you want and run it in any other machine system. For example if you want Ubuntu 20.4 you can have it in a mac or windows machine or other operating systems. <br>
To get started with Docker for the churn prediction project you can follow the instructions below.

![06-docke](./images/06-docker.png)

### Ubuntu

```bash
sudo apt-get install docker.io
```

To run docker without `sudo`, follow [this instruction](https://docs.docker.com/engine/install/linux-postinstall/).

### Windows

To install the Docker you can just follow the instruction by Andrew Lock in this link: https://andrewlock.net/installing-docker-desktop-for-windows/.

If you are using a subsystem, and the integration fails when running Docker for the first time, make sure your distribution is enabled in the resources settings.

### MacOS

Follow the steps in the [Docker docs](https://docs.docker.com/desktop/install/mac-install/).

To test docker image in terminal, exceute the command:

> docker run -it --rm python:3.9-slim

First the image will be pulled to your machine with `python:3.9-slim` version, then access the python (since the default command is `python`). `rm` tag is to remove the container after using.

To access the `bash`/`terminal` of this image, execute:

> docker run -it --rm --entrypoint=bash python:3.9-slim

Whatever we do in docker container, it has no affect to our local machine.

## Notes

- Once our project was packed in a Docker container, we're able to run our project on any machine.
- First we have to make a Docker image. In Docker image file there are settings and dependecies we have in our project. To find Docker images that you need you can simply search the [Docker](https://hub.docker.com/search?type=image) website.

Here a Dockerfile (There should be no comments in Dockerfile, so remove the comments when you copy)

```docker
# First install the python 3.8, the slim version uses less space
FROM python:3.8.12-slim

# Install pipenv library in Docker
RUN pip install pipenv

# create a directory in Docker named app and we're using it as work directory
WORKDIR /app

# Copy the Pip files into our working derectory
COPY ["Pipfile", "Pipfile.lock", "./"]

# install the pipenv dependencies for the project and deploy them.
RUN pipenv install --deploy --system

# Copy any python files and the model we had to the working directory of Docker
COPY ["*.py", "model_C=1.0.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it
EXPOSE 9696

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
```

The flags `--deploy` and `--system` make sure that we install the dependencies directly inside the Docker container without creating an additional virtual environment (which `pipenv` does by default).

If we don't put the last line `ENTRYPOINT`, we will be in a python shell.

In terminal we run this command to excute the script:

> gunicorn --bind==0.0.0.0:9696 predict:app

Note that for the entrypoint, we put our commands in double quotes and separate by comma. And in docker file it should be like this:

> ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]

After creating the Dockerfile, we need to build it:

```bash
docker build -t zoomcamp-test .
```

To run the image and access it's terminal (replace the entrypoint in dockerfile):

```bash
docker run -it --rm --entrypoint=bash zoomcamp-test
```

To run it, execute the command below. In order to access the URL, we need to expose the port to open for the host machine.

```bash
docker run -it -p 9696:9696 zoomcamp-test:latest
```

![06-docker-port-mapping](./images/06-docker-port-mapping.png)

Flag explanations:

- `-t`: is used for specifying the tag name "zoomcamp-test".
- `-it`: in order for Docker to allow us access to the terminal.
- `--rm`: allows us to remove the image from the system after we're done.
- `-p`: to map the 9696 port of the Docker to 9696 port of our machine. (first 9696 is the port number of our machine and the last one is Docker container port.)
- `--entrypoint=bash`: After running Docker, we will now be able to communicate with the container using bash (as you would normally do with the Terminal). Default is `python`.

At last you've deployed your prediction app inside a Docker container. Congratulations 🥳

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

- [Notes from Peter Ernicke](https://knowmledge.com/2023/10/14/ml-zoomcamp-2023-deploying-machine-learning-models-part-6/)

## Navigation

- [Machine Learning Zoomcamp course](../)
- [Session 5: Deploying Machine Learning Models](./)
- Previous: [Python virtual environment: Pipenv](05-pipenv.md)
- Next: [Deployment to the cloud: AWS Elastic Beanstalk (optional)](07-aws-eb.md)
