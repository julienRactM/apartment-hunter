FROM python:3.8.12

# Set working directory in the container
WORKDIR /app

# Copy model code and requirements file
COPY app.py /app/app.py
COPY script.py /app/script.py
COPY app_model /app/app_model
COPY data /app/data
COPY static /app/static
COPY templates /app/templates

COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Define command to run your model
CMD ["python", "app.py"]
