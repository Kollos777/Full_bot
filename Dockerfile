FROM python:3.10
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["python", "personal_assistant.main"]