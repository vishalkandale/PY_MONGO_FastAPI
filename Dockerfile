# Base Image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variables
ENV PYTHONUNBUFFERED=1

# Expose the port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]

