# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's port
EXPOSE 8080

# Start the app
CMD ["python", "app.py"]
