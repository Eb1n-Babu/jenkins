# Use official Python image
FROM python:3.13.3

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (for caching)
COPY django_app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Django project
COPY django_app/ .

# Expose Django’s default port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]