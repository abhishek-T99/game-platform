FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN pip install --no-cache-dir uv
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt
RUN opentelemetry-bootstrap -a install   # installs Django/WSGI auto-instrumentation

COPY . .
RUN chmod +x entrypoint.sh
RUN DATABASE_URL=postgres://x:x@localhost/x python manage.py collectstatic --noinput
# production: CMD ["./entrypoint.sh"]