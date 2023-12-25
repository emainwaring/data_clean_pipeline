FROM python:3.9
WORKDIR /app

# Copy the Python script to the container
COPY test_sql_connection.py /app/

# Install ODBC drivers and other dependencies
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-archive-keyring.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/debian/10/prod buster main" > /etc/apt/sources.list.d/microsoft-prod.list
RUN apt-get update && apt-get install -y unixodbc-dev
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Run the Python script
CMD ["python", "test_sql_connection.py"]
