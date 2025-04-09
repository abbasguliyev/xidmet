FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser -D xidmet
USER xidmet

EXPOSE 8000

CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8000"]