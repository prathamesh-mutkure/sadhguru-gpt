# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the Python script to the working directory
COPY main.py .

# Copy the .env file to the working directory
COPY .env .

# Install the required dependencies
RUN pip install --no-cache-dir -r requiremts.txt

# Set the entry point for the container
ENTRYPOINT ["python", "main.py"]