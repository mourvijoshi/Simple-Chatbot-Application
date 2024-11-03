# Specify the parent image from which we build
FROM python:3.10

# Set the working directory
WORKDIR /LLM_application_chatbot


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


EXPOSE 5000

CMD ["python", "app.py"]
