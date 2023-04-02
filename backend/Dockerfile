FROM python:3.8

# Setup working directory
RUN mkdir -p /app
WORKDIR /app

# Copy all files in directory
COPY . ./

# Install dependencies
RUN python3 -m pip install -r requirements.txt

# Use eventlet as workers
CMD ["gunicorn", "app:app", "-k", "eventlet", "-b", "0.0.0.0:80", "--keep-alive", "30", "--access-logfile", "-"]
