# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the Python script to the working directory
COPY main.py .

# Copy the .env file to the working directory
COPY .env .

# Install the required dependencies
RUN pip install google-generativeai python-dotenv Flask Flask-CORS

# Set the entry point for the container
ENTRYPOINT ["python", "main.py"]