FROM svizor/zoomcamp-model:3.11.5-slim

# Install pipenv library in Docker
RUN pip install pipenv

# create a directory in Docker named app and we're using it as work directory
WORKDIR /app

# Copy the Pip files into our working derectory
COPY ["Pipfile", "Pipfile.lock",  "./"]

# install the pipenv dependencies for the project and deploy them.
RUN pipenv install --deploy --system

# Copy any python files and the model we had to the working directory of Docker
COPY ["q4_flask_host.py", "model1.bin", "dv.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it
EXPOSE 9696

# If we run the Docker image, we want our predict app to be running
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "q4_flask_host:app"]