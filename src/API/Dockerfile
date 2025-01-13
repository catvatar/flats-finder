FROM python:3.12-bullseye

RUN apt-get update && apt-get install -y \
    firefox-esr

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN mkdir /src
COPY ./src ./src
WORKDIR /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
