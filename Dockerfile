FROM python:3.10-slim
WORKDIR /app
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "personal_assistant/main.py"]
