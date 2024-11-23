FROM python:3.7-alpine
WORKDIR /app

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy application files
COPY . .

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev build-base \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run Flask application
CMD ["flask", "run"]

