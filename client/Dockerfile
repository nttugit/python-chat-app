# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY client.py /app/client.py

# Command to run the client.py script
CMD ["python", "client.py", "172.17.0.2", "13979"]
