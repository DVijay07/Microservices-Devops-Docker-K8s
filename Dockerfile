


From python:3.10-slim

WORKDIR /app

Copy worker.py .

Run pip install  redis

CMD ["python", "worker.py"]

