
From python:3.10-slim

WORKDIR /app

Copy ../requirements.txt .

Run pip install  -r requirements.txt

Copy app.py .

CMD ["python", "app.py"]

