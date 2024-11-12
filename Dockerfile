# Use Google Cloud SDK's container as the base image
FROM google/cloud-sdk

# Set metadata
LABEL maintainer="sidpawar@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install python3-venv and create & use a virtual environment
RUN apt-get update -y && \
    apt-get install -y python3-venv python3-pip && \
    python3 -m venv /opt/venv

# Activate virtual environment and install requirements
ENV PATH="/opt/venv/bin:$PATH"
RUN . /opt/venv/bin/activate && \
    pip3 install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

# Expose the port
EXPOSE ${PORT}

# Start the application with gunicorn
CMD gunicorn --workers 1 --threads 8 --timeout 0 --bind=0.0.0.0:${PORT} app:app