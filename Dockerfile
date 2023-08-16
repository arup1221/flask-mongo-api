
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000

# Define environment variables (MongoDB Atlas credentials or other config if needed)
ENV MONGO_URI="mongodb+srv://arup:arup2345@cluster0.131i8tz.mongodb.net/?retryWrites=true&w=majority"

# Run app.py when the container launches, and specify the port
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]