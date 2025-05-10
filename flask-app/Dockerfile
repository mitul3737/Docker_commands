# Use Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
RUN mkdir -p /opt/source-code
WORKDIR /opt/source-code

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Set environment variables
ENV FLASK_APP=/opt/source-code/app.py
ENV FLASK_ENV=development

# Expose Flask default port
EXPOSE 5000

# Entrypoint command
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
