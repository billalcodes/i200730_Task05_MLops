# Use the official Python image as the base image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files to the working directory
COPY . .

# Expose port 5000 (assuming your Flask app runs on port 5000)
EXPOSE 5000

# Command to start the backend server
CMD ["python", "app.py"]
