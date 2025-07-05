#build backend
FROM python:3.11-slim  
WORKDIR /app
#run apt to ensure psycog2 runs without error
RUN apt-get update && apt-get install -y \
     gcc \
     libpq-dev \
     && rm -rf /var/lib/apt/lists/*
#install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#copy source code
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]

