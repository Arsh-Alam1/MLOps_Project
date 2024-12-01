FROM python:3.8-slim

WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install required Python libraries
RUN pip install -r requirements.txt

# Copy all the other files into the container
COPY . .

# Command to run the Flask app
CMD ["python", "app.py"]

