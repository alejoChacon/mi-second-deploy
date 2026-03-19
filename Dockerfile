FROM python:3.12

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecutamos collectstatic para que se cree la carpeta 'staticfiles' dentro de la imagen
# Usamos --noinput para que el proceso no se detenga pidiendo confirmación
RUN python manage.py collectstatic --noinput

CMD [ "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000" ]