# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY server.py /app/server.py

# Run the server.py script with the given command
CMD ["python", "server.py", "0.0.0.0", "13979"]
