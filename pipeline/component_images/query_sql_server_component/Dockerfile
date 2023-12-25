FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-archive-keyring.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/debian/10/prod buster main" > /etc/apt/sources.list.d/microsoft-prod.list
RUN apt-get update && apt-get install -y unixodbc-dev
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17
RUN pip install -r requirements.txt
ENV CONNECTION_STRING="DRIVER={ODBC Driver 17 for SQL Server};SERVER=your-host-name;DATABASE=dataout;UID=userr;PWD=pass"
