# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY requirements.txt Pipfile.lock /app/

# Install pipenv and project dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Specify the command to run on container start
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
