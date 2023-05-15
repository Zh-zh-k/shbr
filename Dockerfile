FROM python:3.10-alpine3.17 as builder
RUN python3 -m venv /app
RUN source /app/bin/activate
RUN /app/bin/pip install -Us pip
COPY requirements.txt /mnt/
RUN /app/bin/pip3 install -r /mnt/requirements.txt
FROM python:3.10-alpine3.17 as app
WORKDIR /app
COPY --from=builder /app /app
COPY . .
EXPOSE 8080
COPY ./store /apps/store
RUN /app/bin/python3 /apps/store/manage.py makemigrations
RUN /app/bin/python3 /apps/store/manage.py migrate 
RUN /app/bin/python3 /apps/store/manage.py runserver 
CMD /app/bin/uvicorn app.main:app --host=0.0.0.0 --port=8080
