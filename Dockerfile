FROM python:3.11-slim

#set the working directory
WORKDIR /app
#copy the requirements file into the container
COPY requirements.txt .
#install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#copy the rest of the application code into the container
COPY . .
#expose the port the app runs on
EXPOSE 8000
#run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

