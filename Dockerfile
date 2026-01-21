FROM python:3.9-slim
WORKDIR /app
COPY appy.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "appy.py"]
