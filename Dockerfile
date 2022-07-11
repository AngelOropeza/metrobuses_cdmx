FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --user -r requirements.txt --no-cache-dir

COPY app /app/app

RUN rm /app/main.py