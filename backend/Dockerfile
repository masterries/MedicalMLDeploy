
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8881

# Befehl zum Starten der Anwendung
CMD ["uvicorn", "backendapi:app", "--host", "0.0.0.0", "--port", "8881"]
